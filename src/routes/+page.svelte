<script lang="ts">
  import { invoke } from "@tauri-apps/api/core";
  import { FileDialogUtil } from "$lib/util/dialog/file";
  import { VALID_MUSIC_FILE_EXTENSIONS, PEDAL_KIND_MAP } from "../lib/constant";
  import ChorusParameterForm from "$lib/component/form/ChorusParameterForm.svelte";
  import CompressorParameterForm from "$lib/component/form/CompressorParameterForm.svelte";
  import DistortionParameterForm from "$lib/component/form/DistortionParameterForm.svelte";
  import DelayParameterForm from "$lib/component/form/DelayParameterForm.svelte";
  import ReverbParameterForm from "$lib/component/form/ReverbParameterForm.svelte";
  import PhaserParameterForm from "$lib/component/form/PhaserParameterForm.svelte";
  import type { Pedal } from "../lib/pedal-type";
  import { v4 as uuidv4 } from "uuid";
  import TrashIcon from "$lib/component/icon/TrashIcon.svelte";

  function selectPedal(id: string) {
    selectedPedalId = id;
  }

  function selectLatestPedal() {
    selectPedal(pedals.slice(-1)[0].id);
  }

  function addChorus() {
    pedals.push({ id: uuidv4(), name: "", kind: "chorus", parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } });
    pedals = pedals;
    selectLatestPedal();
  }

  function addCompressor() {
    pedals.push({
      id: uuidv4(),
      name: "",
      kind: "compressor",
      parameters: { ratio: 1, threshold: 1, release: 1, attack: 1 },
    });
    pedals = pedals;
    selectLatestPedal();
  }

  function addDelay() {
    pedals.push({ id: uuidv4(), name: "", kind: "delay", parameters: { time: 1, mix: 1, feedback: 1 } });
    pedals = pedals;
    selectLatestPedal();
  }

  function addDistortion() {
    pedals.push({ id: uuidv4(), name: "", kind: "distortion", parameters: { gain: 1 } });
    pedals = pedals;
    selectLatestPedal();
  }

  function addPhaser() {
    pedals.push({ id: uuidv4(), name: "", kind: "phaser", parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } });
    pedals = pedals;
    selectLatestPedal();
  }

  function addReverb() {
    pedals.push({ id: uuidv4(), name: "", kind: "reverb", parameters: { roomSize: 1 } });
    pedals = pedals;
    selectLatestPedal();
  }

  function deletePedal() {
    pedals = pedals.filter((pedal) => pedal.id != selectedPedalId);
  }

  async function applyEffects() {
    const inputFilePath = await FileDialogUtil.selectInputFilePath(
      "エフェクトを適用するファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!inputFilePath) {
      /* message dialog */
      return;
    }

    const outputFilePath = await FileDialogUtil.selectOutputFilePath(
      "エフェクト適用後のファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!outputFilePath) {
      /* message dialog */
      return;
    }

    if (inputFilePath == outputFilePath) {
      /* overwrite message dialog */
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
    <div class="flex-none">
      <button class="btn" on:click={applyEffects}>apply</button>
    </div>
  </div>
  <div class="overflow-x-auto mb-5">
    <ul class="steps">
      <li data-content="" class="step">start</li>
      {#each pedals as { id, name, kind }, index}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        <li class="step pedal-step" data-content={PEDAL_KIND_MAP[kind]} on:click={() => selectPedal(id)}></li>
      {/each}
      <li data-content="" class="step">end</li>
    </ul>
  </div>
  {#if selectedPedal}
    <div>
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
    <div>
      <button class="btn btn-error" on:click={deletePedal}>
        <TrashIcon />
      </button>
    </div>
  {/if}
</div>

<style>
  .pedal-step {
    cursor: pointer;
  }
</style>
