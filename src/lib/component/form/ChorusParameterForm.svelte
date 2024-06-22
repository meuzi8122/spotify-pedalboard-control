<script lang="ts">
  import type { Pedal } from "../../pedal-type";

  export let parameters: Pedal["parameters"];
</script>

<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Rate</span>
    <span class="label-text-alt">{parameters.rate}Hz</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.rate} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Depth</span>
    <span class="label-text-alt">{parameters.depth}</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.depth} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Feedback</span>
    <span class="label-text-alt">{parameters.feedback}</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.feedback} />
</div>
<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Mix</span>
    <span class="label-text-alt">{parameters.mix}</span>
  </label>
  <input type="range" class="range" min="0" max="100" bind:value={parameters.mix} />
</div>
