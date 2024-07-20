<script lang="ts">
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: { [key: string]: number };
</script>

<div class="card bg-base-100 w-full shrink-0 shadow-2xl">
  <div class="card-body">
    <h2 class="card-title">Delay Parameters</h2>
    <div class="flex flex-col">
      <div class="flex space-x-3">
        <ParameterControl label="Delay Time" bind:value={parameters.time} unit="ms" />
        <ParameterControl label="Feedback" bind:value={parameters.feedback} />
        <ParameterControl label="Mix" bind:value={parameters.mix} />
      </div>
    </div>
  </div>
</div>
