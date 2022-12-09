class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def touches(self, position):
        return (
            abs(self.x - position.x) <= 1
            and abs(self.y - position.y) <= 1
        )
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        return f'<Position {self.x},{self.y}>'


class Knot:
    def __init__(self, position: Position) -> None:
        self.position = position
    
    def move(self, direction, number: int):
        if direction == 'R':
            self.position.x += number
        elif direction == 'L':
            self.position.x -= number
        elif direction == 'U':
            self.position.y += number
        elif direction == 'D':
            self.position.y -= number
    
    def batch_move(self, input):
        for move in input.strip().split('\n'):
            direction, number = move.split()
            self.move(direction, int(number))


class Tail(Knot):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.historical_positions = [Position(position.x, position.y)]

    def move(self, direction, number: int):
        for d in direction:
            super().move(d, number)
        self.historical_positions.append(
            Position(self.position.x, self.position.y)
        )


class Head(Knot):
    def __init__(self, position: Position, tail: Tail) -> None:
        super().__init__(position)
        self.tail = tail
    
    def move(self, direction, number: int):
        super().move(direction, number)
        if not self.touching_tail:
            if (self.position.x == self.tail.position.x or
                self.position.y == self.tail.position.y):
                for _ in range(0, number):
                    if not self.touching_tail:
                        self.tail.move(direction, 1)
            else:
                if self.position.x > self.tail.position.x:
                    tail_direction = 'R'
                else:
                    tail_direction = 'L'
                if self.position.y > self.tail.position.y:
                    tail_direction += 'U'
                else:
                    tail_direction += 'D'
                self.tail.move(tail_direction, 1)
                for _ in range(0, number):
                    if not self.touching_tail:
                        self.tail.move(direction, 1)
    
    @property
    def touching_tail(self):
        return self.position.touches(self.tail.position)
