import type { Pedal, PedalKind } from "$lib/type";
import { writable } from "svelte/store";
import { v4 as uuidv4 } from "uuid";

function pedalReducer(kind: PedalKind, id?: string): Pedal {
  const _id = id ? id : uuidv4();

  switch (kind) {
    case "chorus":
      return { id: _id, name: "", kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
    case "compressor":
      return {
        id: _id,
        name: "",
        kind,
        parameters: { ratio: 1, threshold: 1, release: 1, attack: 1 },
      };
    case "delay":
      return { id: _id, name: "", kind, parameters: { time: 1, mix: 1, feedback: 1 } };
    case "distortion":
      return { id: _id, name: "", kind, parameters: { gain: 1 } };
    case "phaser":
      return { id: _id, name: "", kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
    case "reverb":
      return { id: _id, name: "", kind, parameters: { roomSize: 1 } };
  }
}

export const pedals = writable<Pedal[]>([]);

export function addPedal(kind: PedalKind) {
  pedals.update((_pedals) => {
    _pedals.push(pedalReducer(kind));
    return _pedals;
  });
  return;
}

/* Pedal.kindの値はデータバインディングで制御できる */
/* Pedal.kind以外の変更はイベントハンドリングで対応 */

export function updatePedal(id: string) {
  pedals.update((_pedals) => {
    const pedalIndex = _pedals.findIndex((_pedal) => _pedal.id == id);
    _pedals[pedalIndex] = pedalReducer(_pedals[pedalIndex].kind);
    return _pedals;
  });
}

export function deletePedal(id: string) {
  pedals.update((_pedals) => {
    const pedalIndex = _pedals.findIndex((_pedal) => _pedal.id == id);

    if (pedalIndex) {
      _pedals = _pedals.filter((_pedal) => _pedal.id != id);
    }

    return _pedals;
  });
}

export function deleteAllPedals() {
  pedals.update(() => []);
}
