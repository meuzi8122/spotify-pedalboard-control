<script lang="ts">
  import ChorusForm from "$lib/component/form/ChorusForm.svelte";
  import CompressorForm from "$lib/component/form/CompressorForm.svelte";
  import TimeControl from "$lib/component/form/control/TimeControl.svelte";
  import DelayForm from "$lib/component/form/DelayForm.svelte";
  import DistortionForm from "$lib/component/form/DistortionForm.svelte";
  import LimiterForm from "$lib/component/form/LimiterForm.svelte";
  import PhaserForm from "$lib/component/form/PhaserForm.svelte";
  import ReverbForm from "$lib/component/form/ReverbForm.svelte";
  import DeleteIcon from "$lib/component/icon/DeleteIcon.svelte";
  import PlayIcon from "$lib/component/icon/PlayIcon.svelte";
  import PlusIcon from "$lib/component/icon/PlusIcon.svelte";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";
  import type { Kind, Pedal } from "$lib/type";
  import { invoke } from "@tauri-apps/api/core";
  import { v4 } from "uuid";

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

  function addPedal() {
    pedals = [...pedals, pedalReducer("chorus")];
  }

  /* TODO */
  function updatePedal(id: string) {
    const index = pedals.findIndex((pedal) => pedal.id == id);
    pedals[index] = pedalReducer(pedals[index].kind);
    pedals = pedals;
  }

  function deletePedal(id: string) {
    pedals = pedals.filter((pedal) => pedal.id != id);
  }

  async function play() {
    await invoke("play", { sourcePath: "", pedals, startTime, endTime });
  }

  async function save() {
    await invoke("save", { sourcePath: "", pedals, startTime, endTime });
  }

  let startTime: string = "00:00";
  let endTime: string = "00:00";
  let files: FileList;

  let pedals: Pedal[] = [];

  $: isStartTimeInvalid = startTime.match(/[0-9]{2}:[0-9]{2}/) == null;
  $: isEndTimeInvalid = endTime.match(/[0-9]{2}:[0-9]{2}/) == null;
  $: isFormInvalid = isStartTimeInvalid || isEndTimeInvalid;
</script>

<div class="container mx-auto">
  <div class="flex flex-col space-y-3 mb-8">
    <div class="card bg-base-100 w-full shrink-0 shadow-2xl">
      <div class="card-body">
        <h2 class="card-title">Audio</h2>
        <div class="flex flex-col">
          <div class="flex space-x-3">
            <label class="form-control">
              <div class="label">
                <span class="label-text">Source File</span>
              </div>
              <input type="file" class="file-input file-input-bordered" bind:files />
            </label>
            <TimeControl label="Start" bind:time={startTime} />
            <TimeControl label="End" bind:time={endTime} />
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
          <h2 class="card-title">Pedal {index + 1}</h2>
          <div class="flex flex-col">
            <div class="flex space-x-3">
              {#if pedal.kind == "chorus"}
                <ChorusForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "compressor"}
                <CompressorForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "delay"}
                <DelayForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "distortion"}
                <DistortionForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "limiter"}
                <LimiterForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "phaser"}
                <PhaserForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {:else if pedal.kind == "reverb"}
                <ReverbForm
                  bind:kind={pedal.kind}
                  bind:parameters={pedal.parameters}
                  handleChange={() => updatePedal(pedal.id)}
                />
              {/if}
            </div>
          </div>
        </div>
      </div>
    {/each}
  </div>

  <div class="flex justify-end join">
    <button class="btn btn-outline join-item" on:click={addPedal}>
      <PlusIcon />
      Add
    </button>
    <button class="btn btn-outline join-item" on:click={play} disabled={isFormInvalid}>
      <PlayIcon />
      Play
    </button>
    <button class="btn btn-outline join-item" on:click={save} disabled={isFormInvalid}>
      <SaveIcon />
      Save
    </button>
  </div>
</div>
