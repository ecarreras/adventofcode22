import re

class Tester:
    def __init__(self, expression):
        self.expression = expression
    
    def test(self, number: int):
        div_number = re.match(r'divisible by ([0-9]+)', self.expression).groups()[0]
        return number % int(div_number) == 0
    
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
        level = round(level // 3)
        result = self.test.test(level)
        return level, self.result[result]


class MonkeysGroup:
    def __init__(self, input) -> None:
        self.monkeys = []
        for monkey in input.strip().split('\n\n'):
            for attr in monkey.split('\n'):
                attr = attr.strip()
                if re.match(r'Monkey [0-9]+', attr):
                    m = Monkey()
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
        for monkey in self.monkeys:
            while monkey.items:
                item, monkey_idx = monkey.inspect()
                self.monkeys[monkey_idx].items.append(item)
    
    @property
    def monkey_business(self):
        result = 1
        for m in sorted(self.monkeys, key=lambda x: x.inspections, reverse=True)[:2]:
            result *= m.inspections
        return result