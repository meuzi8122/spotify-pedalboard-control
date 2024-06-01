from pedalboard import Chorus, Compressor, Delay, Distortion, Phaser, Reverb
from src.main import PedalBoardGenerator


class TestPedalBoardGenerator:
    def test_generate_pedal_board(self):
        generator = PedalBoardGenerator(
            input_file_path="1.wav",
            effectors=[
                {
                    "name": "chorus",
                    "kind": "chorus",
                    "parameters": {"rate": 0, "depth": 0, "feedback": 0, "mix": 0},
                },
                # ValueError: Compressor "ratio" must be a value >: 1.0
                {
                    "name": "compressor",
                    "kind": "compressor",
                    "parameters": {
                        "threshold": 0,
                        "ratio": 1.0,
                        "attack": 0,
                        "release": 0,
                    },
                },
                {
                    "name": "delay-1",
                    "kind": "delay",
                    "parameters": {"time": 0, "feedback": 0, "mix": 0},
                },
                {"name": "distortion", "kind": "distortion", "parameters": {"gain": 0}},
                {
                    "name": "phaser",
                    "kind": "phaser",
                    "parameters": {"rate": 0, "depth": 0, "feedback": 0, "mix": 0},
                },
                {
                    "name": "reverb",
                    "kind": "reverb",
                    "parameters": {"kind": "reverb", "roomSize": 0},
                },
                # ValueError: Delay (in seconds) must be between 0.0s and 30s.
                {
                    "name": "delay-2",
                    "kind": "delay",
                    "parameters": {"time": 30, "feedback": 0, "mix": 0},
                },
            ],
            output_file_path="2.wav",
        )

        pedal_board = generator._generate_pedal_board()

        assert isinstance(pedal_board[0], Chorus)
        assert isinstance(pedal_board[1], Compressor)
        assert isinstance(pedal_board[2], Delay)
        assert isinstance(pedal_board[3], Distortion)
        assert isinstance(pedal_board[4], Phaser)
        assert isinstance(pedal_board[5], Reverb)
        assert isinstance(pedal_board[6], Delay)
