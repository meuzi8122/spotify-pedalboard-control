<script lang="ts">
  import type { Pedal } from "$lib/store/pedal";

  export let parameters: Pedal["parameters"];
</script>

<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Gain</span>
    <span class="label-text-alt">{parameters.gain}db</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.gain} />
</div>
