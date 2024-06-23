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
  import type { Pedal, PedalKind, SelectEvent } from "$lib/type";
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

  function pedalReducer(kind: PedalKind, id?: string): Pedal {
    const _id = id ? id : uuidv4();

    switch (kind) {
      case "chorus":
        return { id: _id, name: "", kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
      case "compressor":
        return {
          id: _id,
          name: "",
          kind,
          parameters: { ratio: 1, threshold: 1, release: 1, attack: 1 },
        };
      case "delay":
        return { id: _id, name: "", kind, parameters: { time: 1, mix: 1, feedback: 1 } };
      case "distortion":
        return { id: _id, name: "", kind, parameters: { gain: 1 } };
      case "phaser":
        return { id: _id, name: "", kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
      case "reverb":
        return { id: _id, name: "", kind, parameters: { roomSize: 1 } };
    }
  }

  function addPedal(kind: PedalKind) {
    pedals = [...pedals, pedalReducer(kind)];
    selectLatestPedal();
  }

  function deletePedal() {
    pedals = pedals.filter((pedal) => pedal.id != selectedPedalId);
  }

  function deleteAllPedals() {
    pedals = [];
  }

  async function updatePedal(event: SelectEvent) {
    const index = pedals.findIndex((pedal) => pedal.id == selectedPedalId);

    if (index) {
      pedals[index] = pedalReducer(event.currentTarget.value as PedalKind);
      pedals = pedals;
      selectedPedalId = selectedPedalId;
    }
  }

  async function saveEffects() {
    const inputFilePath = await FileDialogUtil.selectInputFilePath(
      "エフェクトを適用するファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!inputFilePath) {
      await message("ファイルが選択されていません。エフェクトの保存を中断します。");
      return;
    }

    /* ファイルの上書きチェックは自動で行われるため不要 */

    const outputFilePath = await FileDialogUtil.selectOutputFilePath("保存先ファイル", VALID_MUSIC_FILE_EXTENSIONS);

    if (!outputFilePath) {
      await message("ファイルが選択されていません。エフェクトの保存を中断します。");
      return;
    }

    await invoke("save_effects", { inputFilePath, outputFilePath, pedals });
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
  const VALID_MUSIC_FILE_EXTENSIONS = [".mp3", ".wav"];
</script>

<div class="container mx-auto">
  <div class="flex mb-5">
    <div class="flex-1 join">
      <button class="btn btn-outline join-item" on:click={() => addPedal("chorus")}>Chorus</button>
      <button class="btn btn-outline join-item" on:click={() => addPedal("compressor")}>Compressor</button>
      <button class="btn btn-outline join-item" on:click={() => addPedal("delay")}>Delay</button>
      <button class="btn btn-outline join-item" on:click={() => addPedal("distortion")}>Distortion</button>
      <button class="btn btn-outline join-item" on:click={() => addPedal("phaser")}>Phaser</button>
      <button class="btn btn-outline join-item" on:click={() => addPedal("reverb")}>Reverb</button>
    </div>
    <div class="join flex-none">
      <button class="btn btn-outline btn-primary join-item" on:click={saveEffects} disabled={hasNoPedals}>
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
    <div class="flex flex-col space-y-3 mb-3">
      <select class="select select-bordered" bind:value={selectedPedal.kind} on:change={updatePedal}>
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
    </div>
    <div class="flex justify-end">
      <button class="btn btn-outline btn-error" on:click={deletePedal}>
        <TrashIcon />
        エフェクターを削除
      </button>
    </div>
  {/if}
</div>
