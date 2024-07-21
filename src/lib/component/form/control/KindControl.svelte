<script lang="ts">
  import type { Kind } from "$lib/type";

  export let kind: Kind;
  export let handleChange;

  const LABELS = [
    { label: "Chorus", kind: "chorus" },
    { label: "Compressor", kind: "compressor" },
    { label: "Delay", kind: "delay" },
    { label: "Distortion", kind: "distortion" },
    { label: "Limiter", kind: "limiter" },
    { label: "Phaser", kind: "phaser" },
    { label: "Reverb", kind: "reverb" },
  ];
</script>

<label class="form-control w-full max-w-xs">
  <div class="label">
    <span class="label-text">Pedal</span>
  </div>
  <select class="select select-bordered" bind:value={kind} on:change={handleChange}>
    {#each LABELS as { label, kind }}
      <option value={kind}>{label}</option>
    {/each}
  </select>
</label>
