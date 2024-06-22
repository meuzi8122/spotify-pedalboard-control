<script lang="ts">
  import { invoke } from "@tauri-apps/api/core";
  import { open, save } from "@tauri-apps/plugin-dialog";

  const VALID_EXTENSIONS = ["wav", "mp3"];

  let inputFilePath: string = "";

  $: inputFileName =
    inputFilePath == ""
      ? "ファイルが選択されていません"
      : inputFilePath.split("\\").at(-1);

  let pedals: any[] = [];

  async function selectInputFile() {
    const _inputFilePath = await open({
      filters: [{ name: "", extensions: VALID_EXTENSIONS }],
    });

    if (_inputFilePath?.path) {
      inputFilePath = _inputFilePath.path;
    }
  }

  async function applyEffects() {
    const outputFilePath = await save({
      filters: [{ name: "", extensions: VALID_EXTENSIONS }],
    });

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
