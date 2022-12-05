class CrateMover9000:
    
    @staticmethod
    def move(stacks, quantity, from_stack, to_stack):
        while quantity:
            element = stacks[from_stack - 1].crates.pop()
            stacks[to_stack - 1].crates.append(element)
            quantity -= 1


class CrateMover9001:
    
    @staticmethod
    def move(stacks, quantity, from_stack, to_stack):
        moves = []
        while quantity:
            element = stacks[from_stack - 1].crates.pop()
            moves.append(element)
            quantity -= 1
        stacks[to_stack - 1].crates.extend(reversed(moves))

class Ship:
    def __init__(self, stacks) -> None:
        self.stacks = stacks
        self.crane = CrateMover9000
    
    def move(self, quantity, from_stack, to_stack):
        self.crane.move(self.stacks, quantity, from_stack, to_stack)
    
    @property
    def message(self):
        return ''.join(s.top for s in self.stacks)
    
    @staticmethod
    def from_string(input: str):
        import re
        elements = []
        for line in input.split('\n'):
            if line.startswith(' 1'):
                continue
            elements += [re.findall(r'( {3,3}|[A-Z]{1}) {0,1}', line)]
        # Initalize stacks
        stacks = [Stack([]) for _ in range(0, len(elements[0]))]
        for row in elements:
            for stack_idx, crate in enumerate(row):
                if crate.strip():
                    stacks[stack_idx].crates.insert(0, crate)

        ship = Ship(stacks)
        return ship
    
    def bulk_moves(self, input):
        import re
        for move in re.findall(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', input):
            # parse to int
            args = [int(x) for x in move]
            self.move(*args)


class Stack:
    def __init__(self, crates=None) -> None:
        if crates is None:
            crates = []
        self.crates = crates
    
    @property
    def top(self):
        return self.crates[-1]