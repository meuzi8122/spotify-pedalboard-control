import { open, save } from "@tauri-apps/plugin-dialog";

export class FileDialogUtil {
  static async selectInputFilePath(extensions: string[]): Promise<string> {
    const inputFilePath = await open({
      filters: [{ name: "", extensions }],
    });

    return inputFilePath?.path ? inputFilePath.path : "";
  }

  static async selectOutputFilePath(
    extensions: string[]
  ): Promise<string | null> {
    const outputFilePath = await save({
      filters: [{ name: "", extensions }],
    });

    return outputFilePath;
  }
}
