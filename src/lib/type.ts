export type Pedal = {
  id: string;
  name: string;
  kind: PedalKind;
  parameters: {
    [key: string]: number;
  };
};

export type PedalKind = "chorus" | "compressor" | "delay" | "distortion" | "phaser" | "reverb";

export type SelectEvent = {
  currentTarget: HTMLSelectElement;
};
