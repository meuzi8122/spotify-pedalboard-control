<script lang="ts">
  import type { Pedal } from "$lib/type";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: Pedal["parameters"];
</script>

<ParameterControl label="Threshold" bind:value={parameters.time} unit="db" />
<ParameterControl label="Ratio" bind:value={parameters.ratio} />
<ParameterControl label="Attack" bind:value={parameters.attack} unit="ms" />
<ParameterControl label="Release" bind:value={parameters.release} />
