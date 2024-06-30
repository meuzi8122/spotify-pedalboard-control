<script lang="ts">
  import { addPedal, deleteAllPedals, pedals } from "$lib/store/pedal";
  import { FileDialogUtil } from "$lib/util/dialog/file";
  import { invoke } from "@tauri-apps/api/core";
  import { message } from "@tauri-apps/plugin-dialog";
  import { VALID_MUSIC_FILE_EXTENSIONS } from "$lib/constant";
  import MenuIcon from "$lib/component/icon/MenuIcon.svelte";
  import "../style.css";

  async function saveEffects() {
    const inputFilePath = await FileDialogUtil.selectInputFilePath(
      "エフェクトを適用するファイル",
      VALID_MUSIC_FILE_EXTENSIONS
    );

    if (!inputFilePath) {
      await message("ファイルが選択されていません。エフェクトの保存を中断します。");
      return;
    }

    /* ファイルの上書きチェックは自動で行われるため不要 */

    const outputFilePath = await FileDialogUtil.selectOutputFilePath("保存先ファイル", VALID_MUSIC_FILE_EXTENSIONS);

    if (!outputFilePath) {
      await message("ファイルが選択されていません。エフェクトの保存を中断します。");
      return;
    }

    let isSuccess = true;

    try {
      await invoke("save_effects", { inputFilePath, outputFilePath, pedals });
    } catch {
      isSuccess = false;
    }

    await message(isSuccess ? "エフェクトを保存しました。" : `エフェクトの保存に失敗しました。`);
  }
</script>

<div class="navbar bg-base-100">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl">PedalBoard</a>
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
      <li><a on:click={saveEffects}>Save</a></li>
      <li><a on:click={deleteAllPedals}>Rest</a></li>
      <li><a on:click={() => addPedal("chorus")}>Chorus</a></li>
      <li><a on:click={() => addPedal("compressor")}>Compressor</a></li>
      <li><a on:click={() => addPedal("delay")}>Delay</a></li>
      <li><a on:click={() => addPedal("distortion")}>Distortion</a></li>
      <li><a on:click={() => addPedal("phaser")}>Phaser</a></li>
      <li><a on:click={() => addPedal("reverb")}>Reverb</a></li>
    </ul>
  </div>
</div>
