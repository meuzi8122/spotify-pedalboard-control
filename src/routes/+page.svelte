<script lang="ts">
  import { invoke } from "@tauri-apps/api/core";
  import { FileDialogUtil } from "../lib/util/dialog/file";

  const VALID_EXTENSIONS = ["wav", "mp3"];

  let inputFilePath: string = "";

  $: inputFileName =
    inputFilePath == ""
      ? "ファイルが選択されていません"
      : inputFilePath.split("\\").at(-1);

  let pedals: any[] = [];

  async function selectInputFile() {
    inputFilePath = await FileDialogUtil.selectInputFilePath(VALID_EXTENSIONS);
  }

  async function applyEffects() {
    const outputFilePath =
      await FileDialogUtil.selectOutputFilePath(VALID_EXTENSIONS);

    if (outputFilePath) {
      await invoke("apply_effects", {
        inputFilePath,
        outputFilePath,
        pedals,
      });
    }
  }
</script>

<p>hello</p>
<button on:click={selectInputFile}>select</button>
<button on:click={applyEffects}>apply</button>
{inputFileName}
