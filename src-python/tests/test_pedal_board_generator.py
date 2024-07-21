from pedalboard import Chorus, Compressor, Delay, Distortion, Limiter, Phaser, Reverb
from src.main import PedalBoardGenerator


class TestPedalBoardGenerator:
    def test_generate_pedal_board(self):
        pedals = [
            {
                "kind": "chorus",
                "parameters": {"rate": 0, "depth": 0, "feedback": 0, "mix": 0},
            },
            {
                "kind": "compressor",
                "parameters": {
                    "threshold": 0,
                    "ratio": 0,
                    "attack": 0,
                    "release": 0,
                },
            },
            {
                "kind": "delay",
                "parameters": {"time": 0, "feedback": 0, "mix": 0},
            },
            {"kind": "distortion", "parameters": {"gain": 0}},
            {
                "kind": "phaser",
                "parameters": {"rate": 0, "depth": 0, "feedback": 0, "mix": 0},
            },
            {
                "kind": "reverb",
                "parameters": {"kind": "reverb", "roomSize": 0},
            },
            {
                "kind": "limit",
                "parameters": {"threshold": 0, "release": 0},
            },
        ]

        pedal_board = PedalBoardGenerator._generate_pedal_board(pedals=pedals)

        assert isinstance(pedal_board[0], Chorus)
        assert isinstance(pedal_board[1], Compressor)
        assert isinstance(pedal_board[2], Delay)
        assert isinstance(pedal_board[3], Distortion)
        assert isinstance(pedal_board[4], Phaser)
        assert isinstance(pedal_board[5], Reverb)
        assert isinstance(pedal_board[6], Limiter)
