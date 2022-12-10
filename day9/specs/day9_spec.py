from mamba import *
from expects import *
from day9.rope import Position, Head, Tail, Grid


with description('Day 9'):
    with description('A position'):
        with description('is equal to other position'):
            with it('should return true'):
                p1 = Position(1, 1)
                p2 = Position(1, 1)
                expect(p1).to(equal(p2))
        with description('is touching another position'):
            with context('when overlapping'):
                with it('should touch return true'):
                    h = Position(0, 0)
                    t = Position(0, 0)
                    expect(h.touches(t)).to(be_true)
            with context('when head is one right from tail'):
                with it('should touch return true'):
                    h = Position(0, 1)
                    t = Position(0, 0)
                    expect(h.touches(t)).to(be_true)
            with context('when head is one right up from tail'):
                with it('should touch return true'):
                    h = Position(1, 1)
                    t = Position(0, 0)
                    expect(h.touches(t)).to(be_true)
            with context('when head is one up from tail'):
                with it('should touch return true'):
                    h = Position(1, 1)
                    t = Position(1, 0)
                    expect(h.touches(t)).to(be_true)
    
    with description('Moving the head'):
        with context('when moving one right'):
            with it('tail should move one position right'):
                t = Tail(Position(1, 1))
                h = Head(Position(2, 1), tail=t)
                h.move('R', 1)
                expect(h.position).to(equal(Position(3, 1)))
                expect(t.position).to(equal(Position(2, 1)))
        with context('when moving one down'):
            with it('tail should move one position down'):
                t = Tail(Position(1, 3))
                h = Head(Position(1, 2), tail=t)
                h.move('D', 1)
                expect(h.position).to(equal(Position(1, 1)))
                expect(t.position).to(equal(Position(1, 2)))
        
        with context('when are in diagonal'):
            with context('when moving one up'):
                with it('tail should move diagonally'):
                    t = Tail(Position(1, 1))
                    h = Head(Position(2, 2), tail=t)
                    h.move('U', 1)
                    expect(h.position).to(equal(Position(2, 3)))
                    expect(t.position).to(equal(Position(2, 2)))
            with context('when moving one right'):
                with it('tail should move diagonally'):
                    t = Tail(Position(1, 1))
                    h = Head(Position(2, 2), tail=t)
                    h.move('R', 1)
                    expect(h.position).to(equal(Position(3, 2)))
                    expect(t.position).to(equal(Position(2, 2)))
        
        with context('When doing a set of movements'):
            with before.all as self:
                t = Tail(Position(0, 0))
                self.h = Head(Position(0, 0), tail=t)
            with context('Moving 4 right'):
                with it('head position is 4,0 and tail is 3,0'):
                    self.h.move('R', 4)
                    expect(self.h.position).to(equal(Position(4, 0)))
                    expect(self.h.tail.position).to(equal(Position(3, 0)))
            with context('Moving 4 up'):
                with it('head position is 4,4 and tail is 4,3'):
                    self.h.move('U', 4)
                    expect(self.h.position).to(equal(Position(4, 4)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 3 left'):
                with it('head position is 1,4 and tail is 2,4'):
                    self.h.move('L', 3)
                    expect(self.h.position).to(equal(Position(1, 4)))
                    expect(self.h.tail.position).to(equal(Position(2, 4)))
            with context('Moving 1 down'):
                with it('head position is 1,3 and tail is 2,4'):
                    self.h.move('D', 1)
                    expect(self.h.position).to(equal(Position(1, 3)))
                    expect(self.h.tail.position).to(equal(Position(2, 4)))
            with context('Moving 4 right'):
                with it('head position is 5,3 and tail is 4,3'):
                    self.h.move('R', 4)
                    expect(self.h.position).to(equal(Position(5, 3)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 1 down'):
                with it('head position is 5,2 and tail is 4,3'):
                    self.h.move('D', 1)
                    expect(self.h.position).to(equal(Position(5, 2)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 5 left'):
                with it('head position is 0,2 and tail is 1,2'):
                    self.h.move('L', 5)
                    expect(self.h.position).to(equal(Position(0, 2)))
                    expect(self.h.tail.position).to(equal(Position(1, 2)))
            with context('Moving 2 right'):
                with it('head position is 2,2 and tail is 1,2'):
                    self.h.move('R', 2)
                    expect(self.h.position).to(equal(Position(2, 2)))
                    expect(self.h.tail.position).to(equal(Position(1, 2)))
            
            with description('Counting a total of tail positions'):
                with it('should be 13'):
                    expect(len(set(self.h.tail.historical_positions))).to(equal(13))
        
        with description('Parsing a batch of movements'):
            with before.all as self:
                input = """
                R 4
                U 4
                L 3
                D 1
                R 4
                D 1
                L 5
                R 2
                """
                t = Tail(Position(0, 0))
                self.h = Head(Position(0, 0), tail=t)
                self.h.batch_move(input)
            
            with description('Counting a total of tail positions'):
                with it('should be 13'):
                    expect(len(set(self.h.tail.historical_positions))).to(equal(13))
    
    with description('Part two'):
        with context('When doing a set of movements'):
            with before.all as self:
                self.h9 = Tail(Position(0, 0))
                self.h8 = Tail(Position(0, 0), tail=self.h9)
                self.h7 = Tail(Position(0, 0), tail=self.h8)
                self.h6 = Tail(Position(0, 0), tail=self.h7)
                self.h5 = Tail(Position(0, 0), tail=self.h6)
                self.h4 = Tail(Position(0, 0), tail=self.h5)
                self.h3 = Tail(Position(0, 0), tail=self.h4)
                self.h2 = Tail(Position(0, 0), tail=self.h3)
                self.h1 = Tail(Position(0, 0), tail=self.h2)
                self.h = Head(Position(0, 0), tail=self.h1)
            with context('Moving 4 right'):
                with it('head position is 4,0 and tail is 3,0'):
                    self.h.move('R', 4)
                    expect(self.h.position).to(equal(Position(4, 0)))
                    expect(self.h1.position).to(equal(Position(3, 0)))
                    expect(self.h2.position).to(equal(Position(2, 0)))
                    expect(self.h3.position).to(equal(Position(1, 0)))
                    expect(self.h4.position).to(equal(Position(0, 0)))
                    expect(self.h5.position).to(equal(Position(0, 0)))
                    expect(self.h6.position).to(equal(Position(0, 0)))
                    expect(self.h7.position).to(equal(Position(0, 0)))
                    expect(self.h8.position).to(equal(Position(0, 0)))
                    expect(self.h9.position).to(equal(Position(0, 0)))
            with context('Moving 4 up'):
                with it('head position is 4,4 and tail is 4,3'):                    
                    self.h.move('U', 4)
                    expect(self.h.position).to(equal(Position(4, 4)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 3 left'):
                with it('head position is 1,4 and tail is 2,4'):
                    self.h.move('L', 3)
                    expect(self.h.position).to(equal(Position(1, 4)))
                    expect(self.h.tail.position).to(equal(Position(2, 4)))
            with context('Moving 1 down'):
                with it('head position is 1,3 and tail is 2,4'):
                    self.h.move('D', 1)
                    expect(self.h.position).to(equal(Position(1, 3)))
                    expect(self.h.tail.position).to(equal(Position(2, 4)))
            with context('Moving 4 right'):
                with it('head position is 5,3 and tail is 4,3'):
                    self.h.move('R', 4)
                    expect(self.h.position).to(equal(Position(5, 3)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 1 down'):
                with it('head position is 5,2 and tail is 4,3'):
                    self.h.move('D', 1)
                    expect(self.h.position).to(equal(Position(5, 2)))
                    expect(self.h.tail.position).to(equal(Position(4, 3)))
            with context('Moving 5 left'):
                with it('head position is 0,2 and tail is 1,2'):
                    self.h.move('L', 5)
                    expect(self.h.position).to(equal(Position(0, 2)))
                    expect(self.h.tail.position).to(equal(Position(1, 2)))
            with context('Moving 2 right'):
                with it('head position is 2,2 and tail is 1,2'):
                    self.h.move('R', 2)
                    expect(self.h.position).to(equal(Position(2, 2)))
                    expect(self.h.tail.position).to(equal(Position(1, 2)))
            
            with description('Counting a total of tail positions'):
                with it('should be 13'):
                    expect(len(set(self.h.tail.historical_positions))).to(equal(13))
        
        with description('Having 9 knots'):
            with before.all as self:
                self.h9 = Tail(Position(11, 5))
                self.h9.name = '9'
                self.h8 = Tail(Position(11, 5), tail=self.h9)
                self.h8.name = '8'
                self.h7 = Tail(Position(11, 5), tail=self.h8)
                self.h7.name = '7'
                self.h6 = Tail(Position(11, 5), tail=self.h7)
                self.h6.name = '6'
                self.h5 = Tail(Position(11, 5), tail=self.h6)
                self.h5.name = '5'
                self.h4 = Tail(Position(11, 5), tail=self.h5)
                self.h4.name = '4'
                self.h3 = Tail(Position(11, 5), tail=self.h4)
                self.h3.name = '3'
                self.h2 = Tail(Position(11, 5), tail=self.h3)
                self.h2.name = '2'
                self.h1 = Tail(Position(11, 5), tail=self.h2)
                self.h1.name = '1'
                self.h = Head(Position(11, 5), tail=self.h1)
                self.h.name = 'H'
                start = Tail(Position(11, 5))
                start.name = 's'
                knots = [
                    self.h, self.h1, self.h2, self.h3, self.h4,
                    self.h5, self.h6, self.h7, self.h8, self.h9,
                    start
                ]
                self.grid = Grid(cols=26, rows=21, knots=knots)
            
            with context('Processing batch'):
                with it('should have 36 positions'):
                    input = """
                    R 5
                    U 8
                    L 8
                    D 3
                    R 17
                    D 10
                    L 25
                    U 20
                    """
                    self.h.batch_move(input)
                    expect(len(set(self.h9.historical_positions))).to(equal(36))


