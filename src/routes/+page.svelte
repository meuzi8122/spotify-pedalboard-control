<script lang="ts">
  import { invoke } from "@tauri-apps/api/core";
  import { save } from "@tauri-apps/plugin-dialog";

  const VALID_EXTENSIONS = [".wav", ".mp3"];

  let inputFilePath: string = "";

  $: inputFileName =
    inputFilePath == ""
      ? "ファイルが選択されていません"
      : inputFilePath.split("\\").at(-1);

  let effectors: any[] = [];

  async function applyEffects() {
    const outputFilePath = await save({
      filters: [{ name: "output-file-filter", extensions: VALID_EXTENSIONS }],
    });

    console.log(outputFilePath);

    if (outputFilePath) {
      await invoke("apply_effects", {
        inputFilePath,
        outputFilePath,
        effectors,
      });
    }
  }
</script>

<p>hello</p>
<button on:click={applyEffects}>apply</button>
