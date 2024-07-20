<script lang="ts">
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: { [key: string]: number };
</script>

<div class="card bg-base-100 w-full shrink-0 shadow-2xl">
  <div class="card-body">
    <h2 class="card-title">Chorus Parameters</h2>
    <div class="flex flex-col">
      <div class="flex space-x-3">
        <ParameterControl label="Rate" bind:value={parameters.rate} />
        <ParameterControl label="Depth" bind:value={parameters.depth} />
        <ParameterControl label="Feedback" bind:value={parameters.feedback} />
        <ParameterControl label="Mix" bind:value={parameters.mix} />
      </div>
    </div>
  </div>
</div>
