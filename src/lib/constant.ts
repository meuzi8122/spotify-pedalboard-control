import type { Kind } from "./type";

export const VALID_AUDIO_FILE_EXTENSIONS = ["mp3", "wav"];

export const KINDS: { name: string; kind: Kind }[] = [
  { name: "Chorus", kind: "chorus" },
  { name: "Compressor", kind: "compressor" },
  { name: "Delay", kind: "delay" },
  { name: "Distortion", kind: "distortion" },
  { name: "Limiter", kind: "limiter" },
  { name: "Phaser", kind: "phaser" },
  { name: "Reverb", kind: "reverb" },
];
