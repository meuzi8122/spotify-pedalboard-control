<script lang="ts">
  export let label: string;
  export let time: string;
</script>

<label class="form-control w-full max-w-xs">
  <div class="label">
    <span class="label-text">{label}</span>
  </div>
  <input type="text" class="input input-bordered w-full max-w-xs" bind:value={time} />
</label>
