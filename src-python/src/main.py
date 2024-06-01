import json
import sys

from src.pedal_board_generator import PedalBoardGenerator

if __name__ == "__main__":
    _, input_file_path, effectors, output_file_path = sys.argv

    generator = PedalBoardGenerator(
        input_file_path=input_file_path,
        effectors=json.loads(effectors),
        output_file_path=output_file_path,
    )

    try:
        generator.apply_effects()
    except Exception as e:
        print(e)
