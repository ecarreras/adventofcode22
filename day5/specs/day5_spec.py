from mamba import *
from expects import *
from day5.supply import Ship, Stack, CrateMover9001


with description('Day 5'):
    with description('A ship with 3 stacks'):
        with before.all as self:
            self.s1 = Stack(['Z', 'N'])
            self.s2 = Stack(['M', 'C', 'D'])
            self.s3 = Stack(['P'])
            self.ship = Ship([self.s1, self.s2, self.s3])
                
        with description('A stack 1'):
            with it('must contains 2 crates'):
                expect(len(self.s1.crates)).to(equal(2))
                expect(self.s1.crates).to(contain_exactly('Z', 'N'))
        with description('A stack 2'):
            with it('must contains 3 crates'):
                expect(len(self.s2.crates)).to(equal(3))
                expect(self.s2.crates).to(contain_exactly('M', 'C', 'D'))
        with description('A stack 3'):
            with it('must contains 3 crates'):
                expect(len(self.s3.crates)).to(equal(1))
                expect(self.s3.crates).to(contain_exactly('P'))
        
        with it('must have 3 stacks'):
            expect(len(self.ship.stacks)).to(equal(3))
        
        with description('Moving elements'):
        
            with description('moving 1 from 2 to 1'):
                with before.all as self:
                    self.ship.move(1, 2, 1)
                with it('stack 1 should have elements Z, N, D'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('Z', 'N', 'D'))
                with it('stack 2 should have elements M, C'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('M', 'C'))
                with it('stack 3 should have elements P'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P'))
            
            with description('moving 3 from 1 to 3'):
                with before.all as self:
                    self.ship.move(3, 1, 3)
                with it('stack 1 should be empty'):
                    expect(self.ship.stacks[0].crates).to(be_empty)
                with it('stack 2 should have elements M, C'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('M', 'C'))
                with it('stack 3 should have elements P, D, N, Z'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'D', 'N', 'Z'))
            
            with description('moving 2 from 2 to 1'):
                with before.all as self:
                    self.ship.move(2, 2, 1)
                with it('stack 1 should have C, M'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('C', 'M'))
                with it('stack 2 should be empty'):
                    expect(self.ship.stacks[1].crates).to(be_empty)
                with it('stack 3 should have elements P, D, N, Z'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'D', 'N', 'Z'))
            
            with description('moving 1 from 1 to 2'):
                with before.all as self:
                    self.ship.move(1, 1, 2)
                with it('stack 1 should have C'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('C'))
                with it('stack 2 should have M'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('M'))
                with it('stack 3 should have elements P, D, N, Z'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'D', 'N', 'Z'))
        
        with description('Getting top elements'):
            with context('stack 1'):
                with it('should be C'):
                    expect(self.ship.stacks[0].top).to(equal('C'))
            with context('stack 2'):
                with it('should be M'):
                    expect(self.ship.stacks[1].top).to(equal('M'))
            with context('stack 3'):
                with it('should be Z'):
                    expect(self.ship.stacks[2].top).to(equal('Z'))
    
        with context('ship to'):
            with it('should be CMZ'):
                expect(self.ship.message).to(equal('CMZ'))
    

    with description('Parsing stacks from text'):
        with before.all:
            input = '\n'.join([
                "    [D]    ",
                "[N] [C]    ",
                "[Z] [M] [P]",
                " 1   2   3 ",
            ])
            self.ship = Ship.from_string(input)
        with context('The ship'):
            with it('should have 3 stacks'):
                expect(len(self.ship.stacks)).to(equal(3))
            with description('A stack 1'):
                with it('must contains 2 crates'):
                    stack = self.ship.stacks[0]
                    expect(len(stack.crates)).to(equal(2))
                    expect(stack.crates).to(contain_exactly('Z', 'N'))
            with description('A stack 2'):
                with it('must contains 3 crates'):
                    stack = self.ship.stacks[1]
                    expect(len(stack.crates)).to(equal(3))
                    expect(stack.crates).to(contain_exactly('M', 'C', 'D'))
            with description('A stack 3'):
                with it('must contains 1 crates'):
                    stack = self.ship.stacks[2]
                    expect(len(stack.crates)).to(equal(1))
                    expect(stack.crates).to(contain_exactly('P'))
            with description('Parsing bulk moves'):
                with before.all as self:
                    input = """
                    move 1 from 2 to 1
                    move 3 from 1 to 3
                    move 2 from 2 to 1
                    move 1 from 1 to 2
                    """
                    self.ship.bulk_moves(input)
                with context('stack 1'):
                    with it('should have C'):
                        expect(self.ship.stacks[0].crates).to(contain_exactly('C'))
                with context('stack 2'):
                    with it('should have M'):
                        expect(self.ship.stacks[1].crates).to(contain_exactly('M'))
                with context('stack 3'):
                    with it('should have elements P, D, N, Z'):
                        expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'D', 'N', 'Z'))
                with context('ship to'):
                    with it('should be CMZ'):
                        expect(self.ship.message).to(equal('CMZ'))

    with description('The CrateMover 9001'):
        with before.all as self:
            self.s1 = Stack(['Z', 'N'])
            self.s2 = Stack(['M', 'C', 'D'])
            self.s3 = Stack(['P'])
            self.ship = Ship([self.s1, self.s2, self.s3])
            self.ship.crane = CrateMover9001
        
        with description('Moving elements'):
        
            with description('moving 1 from 2 to 1'):
                with before.all as self:
                    self.ship.move(1, 2, 1)
                with it('stack 1 should have elements Z, N, D'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('Z', 'N', 'D'))
                with it('stack 2 should have elements M, C'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('M', 'C'))
                with it('stack 3 should have elements P'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P'))
            
            with description('moving 3 from 1 to 3'):
                with before.all as self:
                    self.ship.move(3, 1, 3)
                with it('stack 1 should be empty'):
                    expect(self.ship.stacks[0].crates).to(be_empty)
                with it('stack 2 should have elements M, C'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('M', 'C'))
                with it('stack 3 should have elements P, Z, N, D'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'Z', 'N', 'D'))
            
            with description('moving 2 from 2 to 1'):
                with before.all as self:
                    self.ship.move(2, 2, 1)
                with it('stack 1 should have M, C'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('M', 'C'))
                with it('stack 2 should be empty'):
                    expect(self.ship.stacks[1].crates).to(be_empty)
                with it('stack 3 should have elements P, Z, N, D'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'Z', 'N', 'D'))
            
            with description('moving 1 from 1 to 2'):
                with before.all as self:
                    self.ship.move(1, 1, 2)
                with it('stack 1 should have M'):
                    expect(self.ship.stacks[0].crates).to(contain_exactly('M'))
                with it('stack 2 should have C'):
                    expect(self.ship.stacks[1].crates).to(contain_exactly('C'))
                with it('stack 3 should have elements P, Z, N, D'):
                    expect(self.ship.stacks[2].crates).to(contain_exactly('P', 'Z', 'N', 'D'))
    
        with context('ship to'):
            with it('should be MCD'):
                expect(self.ship.message).to(equal('MCD'))
        