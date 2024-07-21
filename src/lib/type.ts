export type Pedal = {
  id: string;
  name: string;
  kind: Kind;
  parameters: { [key: string]: number };
};

export type Kind = "chorus" | "compressor" | "delay" | "distortion" | "limiter" | "phaser" | "reverb";
