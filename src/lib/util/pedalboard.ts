import { v4 } from "uuid";

export type PedalKind = "chorus" | "compressor" | "delay" | "distortion" | "phaser" | "reverb";

export type Pedal = {
  id: string;
  name: string;
  kind: PedalKind;
  parameters: {
    [key: string]: number;
  };
};

export class PedalBoardUtil {
  static initPedal(kind: PedalKind, id?: string): Pedal {
    const _id = id ? id : v4();
    const name = "";

    switch (kind) {
      case "chorus":
        return { id: _id, name, kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
      case "compressor":
        return {
          id: _id,
          name,
          kind,
          parameters: { ratio: 1, threshold: 1, release: 1, attack: 1 },
        };
      case "delay":
        return { id: _id, name, kind, parameters: { time: 1, mix: 1, feedback: 1 } };
      case "distortion":
        return { id: _id, name, kind, parameters: { gain: 1 } };
      case "phaser":
        return { id: _id, name, kind, parameters: { rate: 1, depth: 1, feedback: 1, mix: 1 } };
      case "reverb":
        return { id: _id, name, kind, parameters: { roomSize: 1 } };
    }
  }

  static getPedalIndex(id: string, pedals: Pedal[]): number {
    const index = pedals.findIndex((pedal) => pedal.id == id);

    /* https://github.com/meuzi8122/pedalboard/issues/10#issuecomment-2226882145 */
    if (index > -1) {
      return index;
    }

    throw Error(`Pedal is not found. (id=${id})`);
  }
}
