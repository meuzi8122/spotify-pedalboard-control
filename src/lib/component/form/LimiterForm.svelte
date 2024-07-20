<script lang="ts">
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: { [key: string]: number };
</script>

<div class="card bg-base-100 w-full shrink-0 shadow-2xl">
  <div class="card-body">
    <h2 class="card-title">Limiter Parameters</h2>
    <div class="flex flex-col">
      <div class="flex space-x-3">
        <ParameterControl label="Threshold" bind:value={parameters.threshold} unit="db" />
        <ParameterControl label="Release" bind:value={parameters.release} unit="ms" />
      </div>
    </div>
  </div>
</div>
