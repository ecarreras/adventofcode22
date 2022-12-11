from mamba import *
from expects import *
from day10.cpu import CPU, Addx, Noop, CRT


with description('Day 10'):
    with description('A CPU'):
        with it('has a register X with default value as 1'):
            cpu = CPU()
            expect(cpu.x).to(equal(1))
        with it('has addx and noop as suported instructions'):
            cpu = CPU()
            expect(cpu.supported_instructions.keys()).to(contain_only('addx', 'noop'))
    
    with description('Instructions'):
        with context('Addx'):
            with it('takes two cycles'):
                expect(Addx.TICKS).to(equal(2))
        with context('Noop'):
            with it('takes one cycle'):
                expect(Noop.TICKS).to(equal(1))
    
    with description('Running a small program'):
        with before.all as self:
            self.cpu = CPU()
            instructions = """
            noop
            addx 3
            addx -5
            """
            self.cpu.load_instructions(instructions)
        with description('The instruccions'):
            with it('must be loaded in correct order'):
                expect(self.cpu.instructions).to(contain_exactly('noop', 'addx 3', 'addx -5'))
        with description('At the start of the first cycle'):
            with context('the noop instruction'):
                with it('begins execution'):
                    self.cpu.tick()
                    expect(self.cpu.cycles).to(equal(1))
                    expect(self.cpu.current_instruction).to(be_a(Noop))
            with context('the x register'):
                with it('must be 1'):
                    expect(self.cpu.x).to(equal(1))
        with description('At the start of the second cycle'):
            with context('the addx 3 instruction'):
                with it('begins execution'):
                    self.cpu.tick()
                    expect(self.cpu.cycles).to(equal(2))
                    expect(self.cpu.current_instruction).to(be_a(Addx))
        with description('During the second cycle'):
            with context('X register'):
                with it('must keep 1'):
                    expect(self.cpu.x).to(equal(1))
        with description('After the third cycle'):
            with context('the addx 3 instruction finishes execution'):
                with it('x register must be 4'):
                    self.cpu.tick()
                    expect(self.cpu.cycles).to(equal(3))
                    expect(self.cpu.x).to(equal(4))
        with description('At the start of the fourth cycle'):
            with context('the addx -5 instruction'):
                with it('begins execution'):
                    self.cpu.tick()
                    expect(self.cpu.cycles).to(equal(4))
                    expect(self.cpu.current_instruction).to(be_a(Addx))
            with context('the x register'):
                with it('must be 4'):
                    expect(self.cpu.x).to(equal(4))
        with description('After the fifth cycle'):
            with context('the addx -5 instruction finishes execution'):
                with context('x register'):
                    with it('must be -1'):
                        self.cpu.tick()
                        expect(self.cpu.cycles).to(equal(5))
                        expect(self.cpu.x).to(equal(-1))
    
    with description('Running a larger program'):
        with before.all as self:
            self.cpu = CPU()
            instructions = """
            addx 15
            addx -11
            addx 6
            addx -3
            addx 5
            addx -1
            addx -8
            addx 13
            addx 4
            noop
            addx -1
            addx 5
            addx -1
            addx 5
            addx -1
            addx 5
            addx -1
            addx 5
            addx -1
            addx -35
            addx 1
            addx 24
            addx -19
            addx 1
            addx 16
            addx -11
            noop
            noop
            addx 21
            addx -15
            noop
            noop
            addx -3
            addx 9
            addx 1
            addx -3
            addx 8
            addx 1
            addx 5
            noop
            noop
            noop
            noop
            noop
            addx -36
            noop
            addx 1
            addx 7
            noop
            noop
            noop
            addx 2
            addx 6
            noop
            noop
            noop
            noop
            noop
            addx 1
            noop
            noop
            addx 7
            addx 1
            noop
            addx -13
            addx 13
            addx 7
            noop
            addx 1
            addx -33
            noop
            noop
            noop
            addx 2
            noop
            noop
            noop
            addx 8
            noop
            addx -1
            addx 2
            addx 1
            noop
            addx 17
            addx -9
            addx 1
            addx 1
            addx -3
            addx 11
            noop
            noop
            addx 1
            noop
            addx 1
            noop
            noop
            addx -13
            addx -19
            addx 1
            addx 3
            addx 26
            addx -30
            addx 12
            addx -1
            addx 3
            addx 1
            noop
            noop
            noop
            addx -9
            addx 18
            addx 1
            addx 2
            noop
            noop
            addx 9
            noop
            noop
            noop
            addx -1
            addx 2
            addx -37
            addx 1
            addx 3
            noop
            addx 15
            addx -21
            addx 22
            addx -6
            addx 1
            noop
            addx 2
            addx 1
            noop
            addx -10
            noop
            noop
            addx 20
            addx 1
            addx 2
            addx 2
            addx -6
            addx -11
            noop
            noop
            noop
            """
            self.cpu.load_instructions(instructions)
            self.cpu.run()
        with context('The signal of 20th cycle'):
            with it('should be 420'):
                expect(self.cpu.signals[20]).to(equal(420))
        with context('The signal of 60th cycle'):
            with it('should be 1140'):
                expect(self.cpu.signals[60]).to(equal(1140))
        with context('During the 100th cycle'):
            with it('should be 1800'):
                expect(self.cpu.signals[100]).to(equal(1800))
        with context('During the 140 cycle'):
            with it('should be 2940'):
                expect(self.cpu.signals[140]).to(equal(2940))
        with context('During the 180 cycle'):
            with it('should be 2880'):
                expect(self.cpu.signals[180]).to(equal(2880))
        with context('During the 220 cycle'):
            with it('should be 3960'):
                expect(self.cpu.signals[220]).to(equal(3960))
        with context('The sum of total signal'):
            with it('should be 13140'):
                expect(self.cpu.total_signal).to(equal(13140))
    
    with description('A CRT with a 40 wide and 6 height'):
        with before.all as self:
            self.crt = CRT(40, 6)
        with it('should have 6 rows screen'):
            expect(len(self.crt.screen)).to(equal(6))
        
        with description('For each cycle'):
            with context('When cycle is 1 the position'):
                with it('should be row 0, pixel 0'):
                    self.crt.tick()
                    expect(self.crt.cycles).to(equal(1))
                    expect(self.crt.row).to(equal(0))
                    expect(self.crt.pixel).to(equal(0))
            with context('When cycle is 240'):
                with it('should be row 5, position -1'):
                    self.crt.cycles = 240
                    expect(self.crt.row).to(equal(5))
                    expect(self.crt.pixel).to(equal(-1))

    
    with description('Running a small program with CRT'):
        with before.all as self:
            self.crt = CRT(40, 6)
            self.cpu = CPU(self.crt)
            instructions = """
            addx 15
            addx -11
            addx 6
            addx -3
            addx 5
            addx -1
            addx -8
            addx 13
            addx 4
            noop
            addx -1
            """
            self.cpu.load_instructions(instructions)
        with description('Durying cycle 1'):
            with context('CRT current row'):
                with it('should paint # at pixel 0'):
                    self.cpu.tick()
                    expect(self.crt.screen[0][0]).to(equal('#'))
        with description('Durying cycle 2'):
            with context('CRT current row'):
                with it('should paint # at pixel 1'):
                    self.cpu.tick()
                    expect(self.crt.screen[0][1]).to(equal('#'))
        with description('Durying cycle 3'):
            with context('CRT current row'):
                with it('should paint . at pixel 2'):
                    self.cpu.tick()
                    expect(self.crt.screen[0][2]).to(equal('.'))
        with describe('Running until the end'):
            with context('CRT current row'):
                with it('should be ##..##..##..##..##..#'):
                    self.cpu.run()
                    expect(''.join(self.crt.screen[0])).to(equal('##..##..##..##..##..#'))


            