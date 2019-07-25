import argparse

from cpu import CPU
from instructions import Instruction

NUM_PRG_BLOCKS = 2
HEADER_SIZE = 16
KB_SIZE = 1024


def main():
    # Setup command line argument parser
    parser = argparse.ArgumentParser(description='NES Emulator.')
    parser.add_argument('rom_path',
                        metavar='R',
                        type=str,
                        help='path to nes rom')

    args = parser.parse_args()

    # TODO validate rom path is correct
    print(args.rom_path)

    # Load rom
    with open(args.rom_path, "rb") as file:
        rom_bytes = file.read()

    # create cpu
    cpu = CPU()

    # TODO unhardcode, pull from rom header

    # program data starts after header
    # and lasts for a set number of 16KB blocka
    instructions = rom_bytes[HEADER_SIZE:HEADER_SIZE +
                             (16 * KB_SIZE * NUM_PRG_BLOCKS)]

    for byte in instructions:
        instruction = Instruction(byte)
        cpu.process_instruction(instruction)
        # break


if __name__ == "__main__":
    main()
