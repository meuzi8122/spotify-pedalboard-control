import { open, save } from "@tauri-apps/plugin-dialog";

export class FileDialogUtil {
  static async selectInputFilePath(name: string, extensions: string[]): Promise<string | null> {
    const inputFilePath = await open({ filters: [{ name, extensions }] });

    return inputFilePath?.path ? inputFilePath.path : null;
  }

  static async selectOutputFilePath(name: string, extensions: string[]): Promise<string | null> {
    const outputFilePath = await save({
      filters: [{ name, extensions }],
    });

    return outputFilePath;
  }
}
