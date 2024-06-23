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
  import ResetIcon from "$lib/component/icon/ResetIcon.svelte";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";
  import TrashIcon from "$lib/component/icon/TrashIcon.svelte";
  import { VALID_MUSIC_FILE_EXTENSIONS } from "$lib/constant";
  import type { Pedal } from "$lib/pedal-type";
  import { FileDialogUtil } from "$lib/util/dialog/file";
  import { invoke } from "@tauri-apps/api/core";
  import { message } from "@tauri-apps/plugin-dialog";
  import { v4 as uuidv4 } from "uuid";

  function selectPedal(id: string) {
    selectedPedalId = id;
  }

  function selectLatestPedal() {
    selectPedal(pedals.slice(-1)[0].id);
  }

  function addChorus() {
    pedals = [
      ...pedals,
      { id: uuidv4(), name: "", kind: "chorus", parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } },
    ];
    selectLatestPedal();
  }

  function addCompressor() {
    pedals = [
      ...pedals,
      { id: uuidv4(), name: "", kind: "compressor", parameters: { ratio: 1, threshold: 1, release: 1, attack: 1 } },
    ];
    selectLatestPedal();
  }

  function addDelay() {
    pedals = [...pedals, { id: uuidv4(), name: "", kind: "delay", parameters: { time: 1, mix: 1, feedback: 1 } }];
    selectLatestPedal();
  }

  function addDistortion() {
    pedals = [...pedals, { id: uuidv4(), name: "", kind: "distortion", parameters: { gain: 1 } }];
    selectLatestPedal();
  }

  function addPhaser() {
    pedals = [
      ...pedals,
      { id: uuidv4(), name: "", kind: "phaser", parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } },
    ];
    selectLatestPedal();
  }

  function addReverb() {
    pedals = [...pedals, { id: uuidv4(), name: "", kind: "reverb", parameters: { roomSize: 1 } }];
    selectLatestPedal();
  }

  function deletePedal() {
    pedals = pedals.filter((pedal) => pedal.id != selectedPedalId);
  }

  function deleteAllPedals() {
    pedals = [];
  }

  async function applyEffects() {
    const inputFilePath = await FileDialogUtil.selectInputFilePath(
      "エフェクトを適用するファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!inputFilePath) {
      await message("ファイルが選択されていません。エフェクトの適用を中断します。");
      return;
    }

    /* ファイルの上書きチェックは自動で行われるため不要 */

    const outputFilePath = await FileDialogUtil.selectOutputFilePath(
      "エフェクト適用後のファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!outputFilePath) {
      await message("ファイルが選択されていません。エフェクトの適用を中断します。");
      return;
    }

    await invoke("apply_effects", { inputFilePath, outputFilePath, pedals });
  }

  let pedals: Pedal[] = [];

  let selectedPedalId: string | null = null;
  $: selectedPedal = (() => {
    if (selectedPedalId == null) {
      return null;
    }

    const _selectedPedal = pedals.find((pedal) => pedal.id == selectedPedalId);
    if (_selectedPedal) {
      return _selectedPedal;
    }

    return null;
  })();

  $: hasNoPedals = pedals.length == 0;

  const STEP_ICON_SIZE = 24;
</script>

<div class="container mx-auto">
  <div class="flex mb-5">
    <div class="flex-1 join">
      <button class="btn btn-outline join-item" on:click={addChorus}>Chorus</button>
      <button class="btn btn-outline join-item" on:click={addCompressor}>Compressor</button>
      <button class="btn btn-outline join-item" on:click={addDelay}>Delay</button>
      <button class="btn btn-outline join-item" on:click={addDistortion}>Distortion</button>
      <button class="btn btn-outline join-item" on:click={addPhaser}>Phaser</button>
      <button class="btn btn-outline join-item" on:click={addReverb}>Reverb</button>
    </div>
    <div class="join flex-none">
      <button class="btn btn-outline btn-primary join-item" on:click={applyEffects} disabled={hasNoPedals}>
        <SaveIcon />
        エフェクトを保存
      </button>
      <button class="btn btn-outline btn-error join-item" on:click={deleteAllPedals} disabled={hasNoPedals}>
        <ResetIcon />
        エフェクトをリセット
      </button>
    </div>
  </div>
  <div class="overflow-x-auto mb-5">
    <ul class="steps my-4">
      <li data-content="" class="step step-primary">
        <GuitarIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
        IN
      </li>
      {#each pedals as { id }, index}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        <li class="step step-secondary pedal-step" data-content="" on:click={() => selectPedal(id)}>
          <PedalIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
          {index + 1}
        </li>
      {/each}
      <li data-content="" class="step step-primary">
        <HeadphoneIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
        OUT
      </li>
    </ul>
  </div>
  {#if selectedPedal}
    <div class="mb-3">
      <p>{selectedPedal.name}</p>
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
    </div>
    <div class="flex justify-end">
      <button class="btn btn-outline btn-error" on:click={deletePedal}>
        <TrashIcon />
        エフェクターを削除
      </button>
    </div>
  {/if}
</div>
