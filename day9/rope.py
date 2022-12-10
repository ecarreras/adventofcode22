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
        if 'R' in direction:
            self.position.x += number
        if 'L' in direction:
            self.position.x -= number
        if 'U' in direction:
            self.position.y += number
        if 'D' in direction:
            self.position.y -= number
    
    def batch_move(self, input):
        for move in input.strip().split('\n'):
            direction, number = move.split()
            self.move(direction, int(number))


class Head(Knot):
    def __init__(self, position: Position, tail) -> None:
        super().__init__(position)
        self.tail = tail
    
    def follow(self, direction):
        if not self.touching_tail:
            if self.position.x == self.tail.position.x:
                self.tail.move(direction[0], 1)
            elif self.position.y == self.tail.position.y:
                self.tail.move(direction[-1], 1)
            else:
                if self.position.y > self.tail.position.y:
                    tail_direction = 'U'
                else:
                    tail_direction = 'D'
                if self.position.x > self.tail.position.x:
                    tail_direction += 'R'
                else:
                    tail_direction += 'L'
                self.tail.move(tail_direction, 1)

    
    def move(self, direction, number: int):
        for _ in range(0, number):
            super().move(direction, 1)
            self.follow(direction)
    
    @property
    def touching_tail(self):
        if not self.tail:
            return True
        return self.position.touches(self.tail.position)


class Tail(Head):
    def __init__(self, position: Position, tail=None) -> None:
        super().__init__(position, tail)
        self.historical_positions = [Position(position.x, position.y)]

    def move(self, direction, number: int):
        super().move(direction, number)
        self.historical_positions.append(
            Position(self.position.x, self.position.y)
        )


class Grid:
    def __init__(self, cols, rows, knots) -> None:
        self.cols = cols
        self.rows = rows
        self.knots = knots
    
    def print(self):
        print()
        print('-- GRID --')
        for y in reversed(range(0, self.rows)):
            row = ''
            for x in range(0, self.cols):
                pos = Position(x, y)
                for knot in self.knots:
                    if knot.position == pos:
                        row += knot.name
                        break
                else:
                    row += '.'
            print(row)
        print('-- END GRID --')
