<script lang="ts">
  import MenuIcon from "$lib/component/icon/MenuIcon.svelte";
  import "../style.css";
</script>

<div class="navbar bg-base-100 mb-8">
  <div class="flex-1">
    <a href="/" class="btn btn-ghost text-xl">Spotify PedalBoard Control</a>
  </div>
  <div class="flex-none">
    <label for="my-drawer-4" class="btn btn-square btn-ghost">
      <MenuIcon />
    </label>
  </div>
</div>

<div class="drawer drawer-end">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <slot></slot>
  </div>
  <div class="drawer-side">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
      <li><a href="/">PedalBoard</a></li>
    </ul>
  </div>
</div>
