<script lang="ts">
  import type { Pedal } from "$lib/type";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: Pedal["parameters"];
</script>

<ParameterControl label="Rate" bind:value={parameters.rate} unit="Hz" />
<ParameterControl label="Depth" bind:value={parameters.depth} />
<ParameterControl label="Feedback" bind:value={parameters.feedback} />
<ParameterControl label="Mix" bind:value={parameters.mix} />
