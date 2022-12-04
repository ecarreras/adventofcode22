class Rucksack:
    def __init__(self, items: str) -> None:
        self.compartments = []
        items_per_compartment = len(items) // 2
        self.compartments.insert(0, items[0:items_per_compartment])
        self.compartments.insert(1, items[items_per_compartment:])
    
    @property
    def items(self):
        return ''.join(self.compartments)
    
    @property
    def errors(self):
        return list(set(self.compartments[0]) & set(self.compartments[1]))
    
    @property
    def priority(self):
        return sum(self.get_priority(e) for e in self.errors)
    

    @staticmethod
    def get_priority(letter):
        import string
        return string.ascii_letters.index(letter) + 1


class RucksackGroup:
    def __init__(self, rucksacks) -> None:
        self.rucksacks = rucksacks
    
    @property
    def badge(self):
        return list(
            set(self.rucksacks[0].items)
            & set(self.rucksacks[1].items)
            & set(self.rucksacks[2].items)
        )[0]
    
    @property
    def priority(self):
        return Rucksack.get_priority(self.badge)


class RuckSacksProcessor:
    def __init__(self, items) -> None:
        self.rucksacks = []
        for item in items.strip().split('\n'):
            self.rucksacks.append(Rucksack(item.strip()))
    
    @property
    def groups(self):
        return [RucksackGroup(self.rucksacks[i:i+3]) for i in range(0, len(self.rucksacks), 3)]
    
    @property
    def group_priority(self):
        return sum(g.priority for g in self.groups)
    
    @property
    def total_priority(self):
        return sum(r.priority for r in self.rucksacks)

