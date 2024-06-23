<script lang="ts">
  import type { Pedal } from "$lib/type";

  export let parameters: Pedal["parameters"];
</script>

<div class="form-control">
  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label class="label">
    <span class="label-text">Delay Time</span>
    <span class="label-text-alt">{parameters.time}ms</span>
  </label>
  <!-- 最大30s(30000ms)まで -->
  <input type="range" class="range" min="0" max="30000" bind:value={parameters.time} />
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
