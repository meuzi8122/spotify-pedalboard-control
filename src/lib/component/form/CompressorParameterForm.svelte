<script lang="ts">
  import type { Pedal } from "$lib/type";

  export let parameters: Pedal["parameters"];
</script>

<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Threshold</span>
    <span class="label-text-alt">{parameters.threshold}db</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.threshold} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Ratio</span>
    <span class="label-text-alt">{parameters.ratio}</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.ratio} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Attack</span>
    <span class="label-text-alt">{parameters.attack}ms</span>
  </label>
  <input type="range" class="range" min="0" max="300" bind:value={parameters.attack} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Release</span>
    <span class="label-text-alt">{parameters.release}ms</span>
  </label>
  <input type="range" class="range" min="0" max="300" bind:value={parameters.release} />
</div>
