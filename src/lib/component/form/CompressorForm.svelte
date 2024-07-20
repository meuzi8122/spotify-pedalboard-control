<script lang="ts">
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: { [key: string]: number };
</script>

<div class="card bg-base-100 w-full shrink-0 shadow-2xl">
  <div class="card-body">
    <h2 class="card-title">Phaser Parameters</h2>
    <div class="flex flex-col">
      <div class="flex space-x-3">
        <ParameterControl label="Threshold" bind:value={parameters.time} unit="db" />
        <ParameterControl label="Ratio" bind:value={parameters.ratio} />
        <ParameterControl label="Attack" bind:value={parameters.attack} unit="ms" />
        <ParameterControl label="Release" bind:value={parameters.release} />
      </div>
    </div>
  </div>
</div>
