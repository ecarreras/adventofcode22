class Instruction:
    TICKS = 0

    def __init__(self, cpu, *args):
        self.cpu = cpu
        self.args = args
    
    def execute(self):
        raise NotImplementedError

class Addx(Instruction):
    TICKS = 2

    def execute(self):
        self.cpu.x += int(self.args[0])


class Noop(Instruction):
    TICKS = 1

    def execute(self):
        pass


class CPU:

    supported_instructions = {
        'addx': Addx,
        'noop': Noop
    }

    def __init__(self) -> None:
        self.x = 1
        self.cycles = 0
        self.idx = 0
        self.instructions = []
        self.current_instruction = None
        self.signals = {}
    
    @property
    def total_signal(self):
        return sum(self.signals.values())

    def tick(self):
        self.cycles += 1
        if not self.current_instruction or not self.current_instruction.TICKS:
            instruction_name, *args = self.instructions[self.idx].split()
            instruction = self.supported_instructions[instruction_name]
            self.current_instruction = instruction(self, *args)
        self.current_instruction.TICKS -= 1
        if (self.cycles % 40) == 20:
            self.signals[self.cycles] = self.cycles * self.x
            
        if not self.current_instruction.TICKS:
            self.current_instruction.execute()
            self.idx += 1
        
    def load_instructions(self, instructions):
        for line in instructions.strip().split('\n'):
            self.instructions.append(line.strip())
    
    def run(self):
        while self.idx < len(self.instructions):
            self.tick()

