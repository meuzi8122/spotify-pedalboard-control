import type { PEDAL_KIND_MAP } from "./constant";

export type Pedal = {
  id: string;
  name: string;
  kind: keyof typeof PEDAL_KIND_MAP;
  parameters: {
    [key: string]: number;
  };
};
