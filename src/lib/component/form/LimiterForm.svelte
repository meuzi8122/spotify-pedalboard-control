<script lang="ts">
  import type { Pedal } from "$lib/type";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: Pedal["parameters"];
</script>

<ParameterControl label="Threshold" bind:value={parameters.threshold} unit="db" />
<ParameterControl label="Release" bind:value={parameters.release} unit="ms" />
