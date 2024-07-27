import tempfile
import librosa
import sounddevice as sd
from pedalboard import Chorus, Compressor, Delay, Distortion, Limiter, Pedalboard, Phaser, Reverb
from pedalboard.io import AudioFile


class PedalBoardGenerator:
    @classmethod
    def save(cls, pedals: list[dict], source_path: str, output_path: str | None = None):
        if not output_path:
            output_path = source_path

        pedal_board = cls._generate_pedal_board(pedals=pedals)

        with AudioFile(source_path) as source_file:
            with AudioFile(
                output_path,
                "w",
                source_file.samplerate,
                source_file.num_channels,
            ) as output_file:
                # 秒単位でエフェクトを適用する
                while source_file.tell() < source_file.frames:
                    chunk = source_file.read(source_file.samplerate)
                    effected = pedal_board(chunk, source_file.samplerate, reset=False)
                    output_file.write(effected)

    @classmethod
    def play(cls, pedals: list[dict], source_path: str):
        with tempfile.TemporaryDirectory() as tmp_dir:
            extension = source_path.split(".")[-1]
            output_path = f"{tmp_dir}/tmp.{extension}"

            cls.save(pedals=pedals, source_path=source_path, output_path=output_path)

            audio, sr = librosa.load(path=output_path)
            sd.play(audio, sr)
            sd.wait()

    @classmethod
    def _generate_pedal_board(pedals: list[dict]) -> Pedalboard:
        pedal_board = Pedalboard()

        for pedal in pedals:
            match pedal:
                case {
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
                    "kind": "distortion",
                    "parameters": {"gain": gain},
                }:
                    pedal_board.append(Distortion(drive_db=gain))
                case {
                    "kind": "limiter",
                    "parameters": {"threshold": threshold, "release": release}
                }:
                    pedal_board.append(Limiter(threshold_db=threshold, release_ms=release))
                case {
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
                    "kind": "reverb",
                    "parameters": {"roomSize": room_size},
                }:
                    pedal_board.append(Reverb(room_size=room_size))

        return pedal_board