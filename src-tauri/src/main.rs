#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod effector;

#[tauri::command]
fn apply_effects(input_file_path: String, output_file_path: String, effectors: Vec<effector::model::Effector>) {
    panic!("{}", input_file_path); 
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![apply_effects])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
