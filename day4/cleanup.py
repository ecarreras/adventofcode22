class Assignment:
    def __init__(self, section_pairs) -> None:
        sections = section_pairs.split(',')
        self.assignments = []
        for section in sections:
            self.assignments.append(range(*self.get_start_end(section)))
    
    @staticmethod
    def get_start_end(section):
        start, end = section.split('-')
        return int(start), int(end) + 1
    
    @property
    def is_contained(self):
        if len(self.assignments[0]) > len(self.assignments[1]):
            return set(self.assignments[1]).issubset(set(self.assignments[0]))
        else:
            return set(self.assignments[0]).issubset(set(self.assignments[1]))
    
    @property
    def overlaps(self):
        return bool(set(self.assignments[0]) & set(self.assignments[1]))


class AssignmentProcessor:
    def __init__(self, input):
        self.assignments = []
        for line in input.strip().split('\n'):
            self.assignments.append(Assignment(line))
    
    @property
    def number_of_contained(self):
        return len([x for x in self.assignments if x.is_contained])
    
    @property
    def number_of_overlaps(self):
        return len([x for x in self.assignments if x.overlaps])
        