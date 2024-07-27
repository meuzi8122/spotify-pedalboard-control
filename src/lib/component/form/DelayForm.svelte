<script lang="ts">
  import type { Pedal } from "$lib/type";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: Pedal["parameters"];
</script>

<ParameterControl label="Delay Time" bind:value={parameters.time} unit="ms" />
<ParameterControl label="Feedback" bind:value={parameters.feedback} />
<ParameterControl label="Mix" bind:value={parameters.mix} />
