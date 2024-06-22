#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod pedal;

use tauri_plugin_shell::ShellExt;

#[tauri::command]
async fn apply_effects(
    app: tauri::AppHandle,
    input_file_path: String,
    output_file_path: String,
    pedals: Vec<pedal::model::Pedal>,
) {
    match serde_json::to_string(&pedals) {
        Ok(json) => {
            let cmd = app.shell().sidecar("main").unwrap().args([
                input_file_path,
                json,
                output_file_path,
            ]);

            //let (mut _rx, mut _child) = cmd.spawn().unwrap();
        }
        Err(err) => panic!("{}", err),
    }
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![apply_effects])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
