from abc import ABC, abstractmethod, abstractproperty


class Instruction(ABC):
    def __init__(self, indentifier_byte: bytes):
        self.indentifier_byte = indentifier_byte

    @abstractproperty
    def instruction_length(self):
        return 1

    @abstractmethod
    def execute(self):
            print("Identifier byte: {}".format(self.indentifier_byte))

class LDAInstruction(Instruction):
    instruction_length = 2
    def execute(self):
        super().execute()

class SEIInstruction(Instruction):
    instruction_length = 1
    def execute(self):
        super().execute()

class CLDInstruction(Instruction):
    instruction_length = 1
    def execute(self):
        super().execute()
