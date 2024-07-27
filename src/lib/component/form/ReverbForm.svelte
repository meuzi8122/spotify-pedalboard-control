<script lang="ts">
  import type { Pedal } from "$lib/type";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let parameters: Pedal["parameters"];
</script>

<ParameterControl label="Room Size" bind:value={parameters.roomSize} />
