import re
import math

class Tester:
    def __init__(self, expression):
        self.expression = expression
    
    def test(self, number: int):
        return number % self.divider == 0

    @property
    def divider(self):
        return int(re.match(r'divisible by ([0-9]+)', self.expression).groups()[0])
    
    def __eq__(self, __o: object) -> bool:
        return self.expression == __o.expression


class Operation:

    def __init__(self, operation: str):
        self.operation = operation
    
    def execute(self, level):
        return eval(self.operation.split('=')[1], {'old': level})
    
    def __eq__(self, __o: object) -> bool:
        return self.operation == __o.operation

class Monkey:
    def __init__(self, items=None, operation=None, test=None, result=None):
        if items is None:
            items = []
        self.items = items
        self._operation = operation
        self._test = test
        if result is None:
            result = {}
        self.result = result
        self.inspections = 0
        self.divide = 3
        self.common_divider = None
    
    @property
    def test(self):
        return Tester(self._test)

    @test.setter
    def test(self, value):
        self._test = value

    @property
    def operation(self):
        return Operation(self._operation)    

    @operation.setter
    def operation(self, value):
        self._operation = value
    
    def inspect(self):
        self.inspections += 1
        item = self.items.pop(0)
        level = self.operation.execute(item)
        level = round(level // self.divide)
        if self.common_divider:
            level = level % self.common_divider
        result = self.test.test(level)
        return level, self.result[result]


class MonkeysGroup:
    def __init__(self, input, divide=3) -> None:
        self.monkeys = []
        for monkey in input.strip().split('\n\n'):
            for attr in monkey.split('\n'):
                attr = attr.strip()
                if re.match(r'Monkey [0-9]+', attr):
                    m = Monkey()
                    m.divide = divide
                elif match := re.match(r'Starting items: (.*)', attr):
                    m.items = [int(x.strip()) for x in match.groups()[0].split(',')]
                elif match := re.match(r'Operation: (.*)', attr):
                    m.operation = match.groups()[0]
                elif match := re.match(r'Test: (.*)', attr):
                    m.test = match.groups()[0]
                elif match := re.match(r'If true: .*([0-9]+)', attr):
                    m.result[True] = int(match.groups()[0])
                elif match := re.match(r'If false: .*([0-9]+)', attr):
                    m.result[False] = int(match.groups()[0])
            self.monkeys.append(m)
    
    def round(self):
        mod_factor = math.prod([monkey.test.divider for monkey in self.monkeys])
        for monkey in self.monkeys:
            monkey.common_divider = mod_factor
            while monkey.items:
                item, monkey_idx = monkey.inspect()
                self.monkeys[monkey_idx].items.append(item)
    
    @property
    def monkey_business(self):
        result = 1
        for m in sorted(self.monkeys, key=lambda x: x.inspections, reverse=True)[:2]:
            result *= m.inspections
        return result
