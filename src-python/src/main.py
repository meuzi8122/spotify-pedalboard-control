import json
import sys

from src.pedal_board_generator import PedalBoardGenerator

if __name__ == "__main__":
    _, source_path, pedals, isSaved = sys.argv

    if isSaved:
        PedalBoardGenerator.save(
            source_path=source_path,
            output_path=source_path,
            pedals=json.loads(pedals),
        )
    else:
        PedalBoardGenerator.play(
            source_path=source_path,
            pedals=json.loads(pedals),
        )
