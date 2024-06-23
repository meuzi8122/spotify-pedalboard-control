<script lang="ts">
  import type { Pedal } from "$lib/type";

  export let parameters: Pedal["parameters"];
</script>

<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Room Size</span>
    <span class="label-text-alt">{parameters.roomSize}</span>
  </label>
  <input type="range" class="range" min="0" max="100" step="0.5" bind:value={parameters.roomSize} />
</div>
