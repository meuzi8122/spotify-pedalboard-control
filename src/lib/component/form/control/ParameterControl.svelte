<script lang="ts">
  export let label: string;
  export let value: number;
  export let unit: string = "";
</script>

<!-- カードからはみ出ないように最大幅を記載 -->

<label class="form-control w-full max-w-xs">
  <div class="label">
    <span class="label-text">{label}</span>
  </div>
  <input type="number" class="input input-bordered w-full max-w-xs" bind:value />
  <div class="label">
    <span class="label-text-alt"></span>
    <span class="label-text-alt">{unit}</span>
  </div>
</label>
