import json
import sys

from src.pedal_board_generator import PedalBoardGenerator

if __name__ == "__main__":
    _, source_path, start_time, end_time, pedals, isSaved = sys.argv

    if isSaved:
        PedalBoardGenerator.save(
            source_path=source_path,
            output_path=source_path,
            start_time=start_time,
            end_time=end_time,
            pedals=json.loads(pedals),
        )
    else:
        PedalBoardGenerator.play(
            source_path=source_path,
            start_time=start_time,
            end_time=end_time,
            pedals=json.loads(pedals),
        )
