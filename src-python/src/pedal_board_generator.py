from pedalboard import Chorus, Compressor, Delay, Distortion, Pedalboard, Phaser, Reverb
from pedalboard.io import AudioFile


class PedalBoardGenerator:
    def __init__(
        self,
        input_file_path: str,
        effectors: list[dict],
        output_file_path: str,
    ) -> None:
        self.input_file_path = input_file_path
        self.effectors = effectors
        self.output_file_path = output_file_path

    def apply_effects(self):
        pedal_board = self._generate_pedal_board()

        with AudioFile(self.input_file_path) as input_file:
            with AudioFile(
                self.output_file_path,
                "w",
                input_file.samplerate,
                input_file.num_channels,
            ) as output_file:
                # 秒単位でエフェクトを適用する
                while input_file.tell() < input_file.frames:
                    chunk = input_file.read(input_file.samplerate)
                    effected = pedal_board(chunk, input_file.samplerate, reset=False)
                    output_file.write(effected)

        print(f"{self.output_file_path}を出力しました。")

    def _generate_pedal_board(self) -> Pedalboard:
        pedal_board = Pedalboard()

        for effector in self.effectors:
            match effector:
                case {
                    "name": name,
                    "kind": "chorus",
                    "parameters": {
                        "rate": rate,
                        "depth": depth,
                        "feedback": feedback,
                        "mix": mix,
                    },
                }:
                    pedal_board.append(Chorus(rate_hz=rate, depth=depth, feedback=feedback, mix=mix))
                case {
                    "name": name,
                    "kind": "compressor",
                    "parameters": {
                        "threshold": threshold,
                        "ratio": ratio,
                        "attack": attack,
                        "release": release,
                    },
                }:
                    pedal_board.append(
                        Compressor(
                            threshold_db=threshold,
                            ratio=ratio,
                            attack_ms=attack,
                            release_ms=release,
                        )
                    )
                case {
                    "name": name,
                    "kind": "delay",
                    "parameters": {"feedback": feedback, "time": time, "mix": mix},
                }:
                    pedal_board.append(
                        Delay(
                            delay_seconds=time,
                            feedback=feedback,
                            mix=mix,
                        )
                    )
                case {
                    "name": name,
                    "kind": "distortion",
                    "parameters": {"gain": gain},
                }:
                    pedal_board.append(Distortion(drive_db=gain))
                case {
                    "name": name,
                    "kind": "phaser",
                    "parameters": {
                        "rate": rate,
                        "depth": depth,
                        "feedback": feedback,
                        "mix": mix,
                    },
                }:
                    pedal_board.append(
                        Phaser(
                            rate_hz=rate,
                            depth=depth,
                            feedback=feedback,
                            mix=mix,
                        )
                    )
                case {
                    "name": name,
                    "kind": "reverb",
                    "parameters": {"roomSize": room_size},
                }:
                    pedal_board.append(Reverb(room_size=room_size))

        return pedal_board
