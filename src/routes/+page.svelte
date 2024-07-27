<script lang="ts">
  import { invoke } from "@tauri-apps/api/core";
  import { message, open } from "@tauri-apps/plugin-dialog";
  import { v4 } from "uuid";
  import ChorusForm from "$lib/component/form/ChorusForm.svelte";
  import CompressorForm from "$lib/component/form/CompressorForm.svelte";
  import DelayForm from "$lib/component/form/DelayForm.svelte";
  import DistortionForm from "$lib/component/form/DistortionForm.svelte";
  import LimiterForm from "$lib/component/form/LimiterForm.svelte";
  import PhaserForm from "$lib/component/form/PhaserForm.svelte";
  import ReverbForm from "$lib/component/form/ReverbForm.svelte";
  import DeleteIcon from "$lib/component/icon/DeleteIcon.svelte";
  import PlayIcon from "$lib/component/icon/PlayIcon.svelte";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";
  import { KINDS, VALID_MUSIC_FILE_EXTENSIONS } from "$lib/constant";
  import type { Kind, Pedal } from "$lib/type";
  import OpenIcon from "$lib/component/icon/OpenIcon.svelte";

  function pedalReducer(kind: Kind, id?: string): Pedal {
    id = id ? id : v4();

    switch (kind) {
      case "chorus":
        return { id, kind, parameters: { rate: 0, depth: 0, feedback: 0, mix: 0 } };
      case "compressor":
        return { id, kind, parameters: { ratio: 0, threshold: 0, release: 0, attack: 0 } };
      case "delay":
        return { id, kind, parameters: { time: 0, mix: 0, feedback: 0 } };
      case "distortion":
        return { id, kind, parameters: { gain: 0 } };
      case "limiter":
        return { id, kind, parameters: { threshold: 0, release: 0 } };
      case "phaser":
        return { id, kind, parameters: { rate: 0, depth: 0, feedback: 0, mix: 0 } };
      case "reverb":
        return { id, kind, parameters: { roomSize: 0 } };
    }
  }

  async function selectAudioFile() {
    const selectedAudioFile = await open({
      filters: [{ name: "Audio File", extensions: VALID_MUSIC_FILE_EXTENSIONS }],
    });

    if (Array.isArray(selectedAudioFile)) {
      audioFilePath = selectedAudioFile[0].name;
    } else if (selectedAudioFile && selectedAudioFile.name) {
      audioFilePath = selectedAudioFile.name;
    } else {
      audioFilePath = null;
    }
  }

  function addPedal(kind: Kind) {
    pedals = [...pedals, pedalReducer(kind)];
  }

  function deletePedal(id: string) {
    pedals = pedals.filter((pedal) => pedal.id != id);
  }

  async function callPedalBoardGenerator(isSaved: boolean) {
    try {
      await invoke("call_pedal_board_generator", {
        sourcePath: "",
        pedals,
        isSaved,
      });
    } catch (err) {
      await message(`${err}`);
    }
  }

  let audioFilePath: string | null = null;

  let pedals: Pedal[] = [];
</script>

<div class="container mx-auto">
  <div class="flex flex-col space-y-3 mb-8">
    <div class="card bg-base-100 w-full shrink-0 shadow-2xl">
      <div class="card-body">
        <h2 class="card-title">Audio File</h2>
        {#if audioFilePath}
          <p>{audioFilePath}</p>
        {:else}
          <p>No audio file chosen</p>
        {/if}
        <div class="card-actions justify-end">
          <button class="btn btn-outline" on:click={selectAudioFile}>
            <OpenIcon />
            Select
          </button>
        </div>
      </div>
    </div>

    <div class="flex flex-col space-y-3 mb-8">
      <div class="card bg-base-100 w-full shrink-0 shadow-2xl">
        <div class="card-body">
          <h2 class="card-title">Add Pedal</h2>
          <p></p>
          <div class="grid gap-2 grid-cols-5">
            {#each KINDS as { name, kind }}
              <button class="btn btn-outline" on:click={() => addPedal(kind)}>{name}</button>
            {/each}
          </div>
        </div>
      </div>
    </div>

    {#each pedals as pedal, index}
      <div class="card bg-base-100 w-full shrink-0 shadow-2xl">
        <div class="card-body">
          <div class="card-actions justify-end">
            <button class="btn btn-square btn-sm" on:click={() => deletePedal(pedal.id)}>
              <DeleteIcon />
            </button>
          </div>
          <h2 class="card-title">Pedal-{index + 1} ({pedal.kind})</h2>
          <div class="flex flex-col">
            <div class="flex space-x-3">
              {#if pedal.kind == "chorus"}
                <ChorusForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "compressor"}
                <CompressorForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "delay"}
                <DelayForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "distortion"}
                <DistortionForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "limiter"}
                <LimiterForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "phaser"}
                <PhaserForm bind:parameters={pedal.parameters} />
              {:else if pedal.kind == "reverb"}
                <ReverbForm bind:parameters={pedal.parameters} />
              {/if}
            </div>
          </div>
        </div>
      </div>
    {/each}
  </div>

  <div class="flex justify-end join">
    <button class="btn btn-outline join-item" on:click={() => callPedalBoardGenerator(false)}>
      <PlayIcon />
      Play
    </button>
    <button class="btn btn-outline join-item" on:click={() => callPedalBoardGenerator(true)}>
      <SaveIcon />
      Save
    </button>
  </div>
</div>
