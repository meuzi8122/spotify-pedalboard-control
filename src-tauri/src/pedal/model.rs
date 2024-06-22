use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/* コマンドはフロントから何のエフェクターを渡されたかを見ない（実行ファイルにそのまま渡すだけ）*/
/* エフェクターの種類ごとに構造体を作る必要はなさそう。 */

#[derive(Debug, Serialize, Deserialize)]
pub struct Pedal {
    name: String,
    kind: String,
    parameters: HashMap<String, isize>,
}
