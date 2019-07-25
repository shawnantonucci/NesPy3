from instruction import LDAInstruction
from rom import ROM


class CPU(object):
    def __init__(self):
        # TODO proper registers
        self.registers = []

        # program counter stores current execution point
        self.running = True
        self.pc = None

        self.instruction_mapping = {
            169: LDAInstruction
        }

        self.rom = None

    def run_rom(self, rom: ROM):
        # load rom
        self.rom = rom
        self.pc = self.rom.header_size

        # run program
        self.running = True
        while self.running:
            # get current byte
            indentifier_byte = self.rom.get_byte(self.pc)

            # turn byte into instruction
            instruction = self.instruction_mapping.get(indentifier_byte, None)
            if instruction is None:
                raise Exception("Instruction not found")
