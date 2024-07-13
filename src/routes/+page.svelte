<script lang="ts">
  import ChorusParameterForm from "$lib/component/form/ChorusParameterForm.svelte";
  import CompressorParameterForm from "$lib/component/form/CompressorParameterForm.svelte";
  import DelayParameterForm from "$lib/component/form/DelayParameterForm.svelte";
  import DistortionParameterForm from "$lib/component/form/DistortionParameterForm.svelte";
  import PhaserParameterForm from "$lib/component/form/PhaserParameterForm.svelte";
  import ReverbParameterForm from "$lib/component/form/ReverbParameterForm.svelte";
  import GuitarIcon from "$lib/component/icon/GuitarIcon.svelte";
  import HeadphoneIcon from "$lib/component/icon/HeadphoneIcon.svelte";
  import PedalIcon from "$lib/component/icon/PedalIcon.svelte";
  import PlusIcon from "$lib/component/icon/PlusIcon.svelte";
  import ResetIcon from "$lib/component/icon/ResetIcon.svelte";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";
  import TrashIcon from "$lib/component/icon/TrashIcon.svelte";
  import { VALID_MUSIC_FILE_EXTENSIONS } from "$lib/constant";
  import { DialogUtil } from "$lib/util/dialog";
  import { PedalBoardUtil, type Pedal, type PedalKind } from "$lib/util/pedalboard";
  import { invoke } from "@tauri-apps/api/core";
  import { message } from "@tauri-apps/plugin-dialog";

  let pedals: Pedal[] = [];
  let selectedPedal: Pedal | null = null;

  function addPedal(kind: PedalKind) {
    const pedal = PedalBoardUtil.initPedal(kind);
    pedals = [...pedals, pedal];
    selectPedal(pedal);
  }

  function initPedalParameters() {
    if (selectedPedal) {
      const index = PedalBoardUtil.getPedalIndex(selectedPedal.id, pedals);
      pedals[index] = PedalBoardUtil.initPedal(selectedPedal.kind, selectedPedal.id);
    }
  }

  function deletePedal() {
    if (selectedPedal) {
      pedals = pedals.filter((pedal) => pedal.id != selectedPedal.id);
      selectPedal();
    }
  }

  function deleteAllPedals() {
    pedals = [];
    selectPedal();
  }

  function selectPedal(pedal?: Pedal) {
    selectedPedal = pedal ? pedal : null;
  }

  async function savePedalBoard() {
    const inputFilePath = await DialogUtil.selectInputFilePath(
      "エフェクトを適用するファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!inputFilePath) {
      await message("エフェクトを適用するファイルが選択されていません。");
      return;
    }

    /* ファイルの上書きチェックは自動で行われるため不要 */

    const outputFilePath = await DialogUtil.selectOutputFilePath(
      "エフェクト適用後の保存先ファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!outputFilePath) {
      await message("エフェクト適用後の保存先ファイルが選択されていません。");
      return;
    }

    try {
      await invoke("save_pedal_board", { inputFilePath, outputFilePath, pedals });
    } catch {
      await message("エフェクトの適用に失敗しました。");
      return;
    }

    await message(`エフェクトを適用しました。(保存先: ${outputFilePath})`);
  }

  const STEP_ICON_SIZE = 26;
</script>

<div class="container mx-auto">
  <div class="flex justify-center join mb-3">
    <button class="btn btn-outline join-item" on:click={() => addPedal("chorus")}>
      <PlusIcon />
      Add Pedal
    </button>
    <button class="btn btn-outline join-item" on:click={savePedalBoard}>
      <SaveIcon />
      Save PedalBoard
    </button>
    <button class="btn btn-outline join-item" on:click={deleteAllPedals}>
      <ResetIcon />
      Reset PedalBoard
    </button>
  </div>
  <div class="overflow-x-auto mb-5">
    <div class="flex justify-center">
      <ul class="steps my-4 py-2">
        <li data-content="" class="step step-primary after:!w-12 after:!h-12 after:text-3xl">
          <GuitarIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
          IN
        </li>
        {#each pedals as pedal, index}
          <li
            class="step step-secondary pedal-step after:!w-12 after:!h-12 after:text-3xl"
            data-content=""
            data-testid="pedal-step"
            on:click={() => selectPedal(pedal)}
          >
            <PedalIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
            {index + 1}
          </li>
        {/each}
        <li data-content="" class="step step-primary after:!w-12 after:!h-12 after:text-3xl">
          <HeadphoneIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
          OUT
        </li>
      </ul>
    </div>
  </div>
  {#if selectedPedal}
    <div class="flex flex-col space-y-3">
      <select class="select select-bordered" bind:value={selectedPedal.kind} on:change={initPedalParameters}>
        <option value="chorus">Chorus</option>
        <option value="compressor">Compressor</option>
        <option value="delay">Delay</option>
        <option value="distortion">Distortion</option>
        <option value="phaser">Phaser</option>
        <option value="reverb">Reverb</option>
      </select>
      {#if selectedPedal.kind == "chorus"}
        <ChorusParameterForm parameters={selectedPedal.parameters} />
      {:else if selectedPedal.kind == "compressor"}
        <CompressorParameterForm parameters={selectedPedal.parameters} />
      {:else if selectedPedal.kind == "distortion"}
        <DistortionParameterForm parameters={selectedPedal.parameters} />
      {:else if selectedPedal.kind == "delay"}
        <DelayParameterForm parameters={selectedPedal.parameters} />
      {:else if selectedPedal.kind == "phaser"}
        <PhaserParameterForm parameters={selectedPedal.parameters} />
      {:else if selectedPedal.kind == "reverb"}
        <ReverbParameterForm parameters={selectedPedal.parameters} />
      {/if}
      <div class="flex justify-end">
        <button class="btn btn-outline btn-error" on:click={deletePedal}>
          <TrashIcon />
          Delete
        </button>
      </div>
    </div>
  {/if}
</div>
