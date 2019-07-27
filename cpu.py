from collections import defaultdict

from instruction import LDAInstruction, SEIInstruction, CLDInstruction
from rom import ROM


class CPU(object):
    def __init__(self):
        # TODO proper registers
        self.registers = []

        # program counter stores current execution point
        self.running = True
        self.pc = None

        self.instruction_classes = [
            SEIInstruction,
            CLDInstruction,
            LDAInstruction
        ]

        self.instruction_class_mapping = defaultdict()
        for instruction_class in self.instruction_classes:
            self.instruction_class_mapping[instruction_class.indentifier_byte] = instruction_class

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
            instruction_class = self.instruction_class_mapping.get(
                indentifier_byte, None)
            if instruction_class is None:
                raise Exception("Instruction not found")

            # We have a valid instruction class
            instruction = instruction_class()
            instruction.execute()

            self.pc += instruction.instruction_length
