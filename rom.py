from typing import List

KB_SIZE = 1024


class ROM(object):
    def __init__(self, rom_bytes: List[int]):
        self.header_size = 16

        self.num_prg_blocks = 2

        # program data starts after header
        # and lasts for a set number of 16KB blocka
        self.data_bytes = rom_bytes[self.header_size:self.header_size +
                                    (16 * KB_SIZE * self.num_prg_blocks)]

    def get_byte(self, position: int) -> int:
        """
        gets byte at given position
        """
        return self.data_bytes[position]
