<script lang="ts">
  import { afterNavigate } from "$app/navigation";
  import ChorusForm from "$lib/component/form/ChorusForm.svelte";
  import CompressorForm from "$lib/component/form/CompressorForm.svelte";
  import TimeControl from "$lib/component/form/control/TimeControl.svelte";
  import DelayForm from "$lib/component/form/DelayForm.svelte";
  import LimiterForm from "$lib/component/form/LimiterForm.svelte";
  import PhaserForm from "$lib/component/form/PhaserForm.svelte";
  import ReverbForm from "$lib/component/form/ReverbForm.svelte";
  import PlayIcon from "$lib/component/icon/PlayIcon.svelte";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";

  /** @type {import("./$types").PageData} */
  export let data;

  afterNavigate(() => {
    switch (data.effect) {
      case "chorus":
        parameters = { rate: 1, depth: 1, feedback: 1, mix: 1 };
        break;
      case "compressor":
        parameters = { ratio: 1, threshold: 1, release: 1, attack: 1 };
        break;
      case "delay":
        parameters = { time: 1, mix: 1, feedback: 1 };
      case "limiter":
        parameters = { threshold: 1, release_ms: 1 };
        break;
      case "phaser":
        parameters = { rate: 1, depth: 1, feedback: 1, mix: 1 };
        break;
      case "reverb":
        parameters = { roomSize: 1 };
        break;
      default:
        parameters = {};
        break;
    }
    startTime = "00:00";
    endTime = "00:00";
  });

  function onSave() {}

  let parameters: { [key: string]: number } = {};
  let startTime: string = "00:00";
  let endTime: string = "00:00";
  let files: FileList;

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

    {#if data.effect == "chorus"}
      <ChorusForm bind:parameters />
    {:else if data.effect == "compressor"}
      <CompressorForm bind:parameters />
    {:else if data.effect == "delay"}
      <DelayForm bind:parameters />
    {:else if data.effect == "limiter"}
      <LimiterForm bind:parameters />
    {:else if data.effect == "phaser"}
      <PhaserForm bind:parameters />
    {:else if data.effect == "reverb"}
      <ReverbForm bind:parameters />
    {/if}
  </div>

  <div class="flex">
    <div class="flex-1"></div>
    <div class="flex-none space-x-2">
      <button class="btn btn-outline" disabled={isFormInvalid}>
        <PlayIcon />
        Play
      </button>
      <button class="btn btn-outline" on:click={onSave} disabled={isFormInvalid}>
        <SaveIcon />
        Save
      </button>
    </div>
  </div>
</div>
