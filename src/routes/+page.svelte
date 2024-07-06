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
  import TrashIcon from "$lib/component/icon/TrashIcon.svelte";
  import { deletePedal, pedals, updatePedal } from "$lib/store/pedal";
  import type { Pedal } from "$lib/store/pedal";

  function selectPedal(id: string) {
    if (id == null) {
      return null;
    }

    const _selectedPedal = $pedals.find((pedal) => pedal.id == id);

    if (_selectedPedal) {
      selectedPedal = _selectedPedal;
    }
  }

  function selectLatestPedal() {
    selectPedal($pedals.slice(-1)[0].id);
  }

  function handleUpdatePedal() {
    if (selectedPedal) {
      updatePedal(selectedPedal.id);
    }
  }

  function handleDeletePedal() {
    if (selectedPedal) {
      deletePedal(selectedPedal.id);
      selectLatestPedal();
    }
  }

  let selectedPedal: Pedal | null = null;

  const STEP_ICON_SIZE = 24;
</script>

<div class="container mx-auto">
  <div class="overflow-x-auto mb-5">
    <div class="flex justify-center">
      <ul class="steps my-4">
        <li data-content="" class="step step-primary">
          <GuitarIcon width={STEP_ICON_SIZE} height={STEP_ICON_SIZE} />
          IN
        </li>
        {#each $pedals as { id }, index}
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
          <li
            class="step step-secondary pedal-step"
            data-content=""
            data-testid="pedal-step"
            on:click={() => selectPedal(id)}
          >
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
  </div>
  {#if selectedPedal}
    <div class="flex flex-col space-y-3 mb-3">
      <select class="select select-bordered" bind:value={selectedPedal.kind} on:change={handleUpdatePedal}>
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
      <button class="btn btn-outline btn-error" on:click={handleDeletePedal}>
        <TrashIcon />
        エフェクターを削除
      </button>
    </div>
  {/if}
</div>
