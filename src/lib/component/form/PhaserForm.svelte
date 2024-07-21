<script lang="ts">
  import type { Kind, Pedal } from "$lib/type";
  import KindControl from "./control/KindControl.svelte";
  import ParameterControl from "./control/ParameterControl.svelte";

  export let kind: Kind;
  export let parameters: Pedal["parameters"];

  export let handleChange: (id: string) => void;
</script>

<KindControl bind:kind {handleChange} />
<ParameterControl label="Rate" bind:value={parameters.rate} unit="Hz" />
<ParameterControl label="Depth" bind:value={parameters.depth} />
<ParameterControl label="Feedback" bind:value={parameters.feedback} />
<ParameterControl label="Mix" bind:value={parameters.mix} />
