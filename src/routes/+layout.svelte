<script lang="ts">
  import { addPedal, deleteAllPedals, pedals } from "$lib/store/pedal";
  import { FileDialogUtil } from "$lib/util/dialog/file";
  import { invoke } from "@tauri-apps/api/core";
  import { message } from "@tauri-apps/plugin-dialog";
  import { VALID_MUSIC_FILE_EXTENSIONS } from "$lib/constant";
  import MenuIcon from "$lib/component/icon/MenuIcon.svelte";
  import "../style.css";
  import SaveIcon from "$lib/component/icon/SaveIcon.svelte";
  import ResetIcon from "$lib/component/icon/ResetIcon.svelte";
  import PlusIcon from "$lib/component/icon/PlusIcon.svelte";
  import EditIcon from "$lib/component/icon/EditIcon.svelte";

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
    let error;

    try {
      await invoke("save_pedal_board", { inputFilePath, outputFilePath, $pedals });
    } catch (e) {
      isSuccess = false;
      error = e;
    }

    await message(isSuccess ? "エフェクトを保存しました。" : `エフェクトの保存に失敗しました。${error}`);
  }
</script>

<div class="navbar bg-base-100 mb-8">
  <div class="flex-1">
    <a href="/" class="btn btn-ghost text-xl">PedalBoard</a>
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
      <!-- <li><a on:click={saveEffects}><SaveIcon />Save</a></li>
      <li><a on:click={deleteAllPedals}><ResetIcon />Reset</a></li>
      <li><a on:click={() => addPedal("chorus")}><PlusIcon />Chorus</a></li>
      <li><a on:click={() => addPedal("compressor")}><PlusIcon />Compressor</a></li>
      <li><a on:click={() => addPedal("delay")}><PlusIcon />Delay</a></li>
      <li><a on:click={() => addPedal("distortion")}><PlusIcon />Distortion</a></li>
      <li><a on:click={() => addPedal("phaser")}><PlusIcon />Phaser</a></li>
      <li><a on:click={() => addPedal("reverb")}><PlusIcon />Reverb</a></li> -->
      <li><a href="/"><EditIcon />Edit</a></li>
    </ul>
  </div>
</div>
