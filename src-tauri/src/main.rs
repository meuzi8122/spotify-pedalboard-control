#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod pedal;

use tauri_plugin_shell::ShellExt;

#[tauri::command]
async fn call_pedal_board_generator(
    app: tauri::AppHandle,
    audio_file_path: String,
    pedals: Vec<pedal::model::Pedal>,
    is_saved: bool
) {
    print!("called");
    match serde_json::to_string(&pedals) {
        Ok(stringified_pedals) => {
            let _ = app.shell().sidecar("main").unwrap().args([
                &audio_file_path,
                &stringified_pedals,
                &is_saved.to_string()
            ]);
            print!("audio_file_path={}, pedals={}, is_saved={}", &audio_file_path, &stringified_pedals, &is_saved);
        }
        Err(err) => panic!("{}", err),
    }
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![call_pedal_board_generator])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
