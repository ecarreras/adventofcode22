from mamba import *
from expects import *
from day11.monkeys import Monkey, Operation, Tester, MonkeysGroup

with description('Day 11'):
    with description('A operation matcher'):
        with it('should run an operation sum'):
            op = Operation('new = old + 6')
            result = op.execute(4)
            expect(result).to(equal(10))
        with it('should run an operation sub'):
            op = Operation('new = old - 6')
            result = op.execute(10)
            expect(result).to(equal(4))
        with it('should run an operation mul'):
            op = Operation('new = old * 6')
            result = op.execute(2)
            expect(result).to(equal(12))
    
    with description('A Tester'):
        with it('should test if divisible by 17'):
            t = Tester('divisible by 17')
            expect(t.test(17)).to(be_true)
        with it('should test if divisible by 49'):
            t = Tester('divisible by 49')
            expect(t.test(49 * 2)).to(be_true)

    with description('A Monkey 0'):
        with it('should have starting items 79, 98'):
            m = Monkey([79, 98])
            expect(m.items).to(contain_exactly(79, 98))
        with it('should have an operation'):
            m = Monkey([79, 98], operation='new = old + 6')
            expect(m.operation).to(equal(Operation('new = old + 6')))
        with it('should have a test'):
            m = Monkey([79, 98], test='divisible by 17')
            expect(m.test).to(equal(Tester('divisible by 17')))

        with it('should have a result matrix position'):
            m = Monkey([79, 98], result={True: 2, False: 3})
            expect(m.result[True]).to(equal(2))
            expect(m.result[False]).to(equal(3))
        
        with context('when inspecting'):
            with before.all as self:
                self.m = Monkey(
                    [79, 98],
                    operation='new = old * 19',
                    test='divisible by 23',
                    result={True: 2, False: 3}
                )
                self.result = self.m.inspect()
            with it('must have only one item in the items'):
                expect(self.m.items).to(contain_exactly(98))
            with it('should return a tuple of worring level, and the monkey to put'):
                expect(self.result).to(equal((500, 3)))
    
    with description('A monkey Group'):
        with before.all as self:
            input = """
            Monkey 0:
                Starting items: 79, 98
                Operation: new = old * 19
                Test: divisible by 23
                    If true: throw to monkey 2
                    If false: throw to monkey 3

            Monkey 1:
                Starting items: 54, 65, 75, 74
                Operation: new = old + 6
                Test: divisible by 19
                    If true: throw to monkey 2
                    If false: throw to monkey 0

            Monkey 2:
                Starting items: 79, 60, 97
                Operation: new = old * old
                Test: divisible by 13
                    If true: throw to monkey 1
                    If false: throw to monkey 3

            Monkey 3:
                Starting items: 74
                Operation: new = old + 3
                Test: divisible by 17
                    If true: throw to monkey 0
                    If false: throw to monkey 1
            """
            self.mg = MonkeysGroup(input)
        
        with context('The monkey group'):
            with it('must have 4 monkeys'):
                expect(len(self.mg.monkeys)).to(equal(4))
            with context('Monkey 0'):
                with it('must have starting items 79, 98'):
                    expect(self.mg.monkeys[0].items).to(contain_exactly(79, 98))
                with it('must have operation new = old * 19'):
                    expect(self.mg.monkeys[0].operation).to(equal(Operation('new = old * 19')))
                with it('must have test divisible by 23'):
                    expect(self.mg.monkeys[0].test).to(equal(Tester('divisible by 23')))
                with it('must have result if true -> 2'):
                    expect(self.mg.monkeys[0].result[True]).to(equal(2))
                with it('must have result if false -> 3'):
                    expect(self.mg.monkeys[0].result[False]).to(equal(3))
        
        with description('Making rounds'):
            with context('The first round'):
                with before.all as self:
                    self.mg.round()
                with context('Mokey 0'):
                    with it('must have items 20, 23, 27, 26'):
                        expect(self.mg.monkeys[0].items).to(contain_exactly(20, 23, 27, 26))
                with context('Monkey 1'):
                    with it('must have items 2080, 25, 167, 207, 401, 1046'):
                        expect(self.mg.monkeys[1].items).to(contain_exactly(2080, 25, 167, 207, 401, 1046))
                with context('Monkey 2'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[2].items).to(be_empty)
                with context('Monkey 3'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[3].items).to(be_empty)
            with context('The second round'):
                with before.all as self:
                    self.mg.round()
                with context('Mokey 0'):
                    with it('must have items 695, 10, 71, 135, 350'):
                        expect(self.mg.monkeys[0].items).to(contain_exactly(695, 10, 71, 135, 350))
                with context('Monkey 1'):
                    with it('must have items 43, 49, 58, 55, 362'):
                        expect(self.mg.monkeys[1].items).to(contain_exactly(43, 49, 58, 55, 362))
                with context('Monkey 2'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[2].items).to(be_empty)
                with context('Monkey 3'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[3].items).to(be_empty)
            with context('The third round'):
                with before.all as self:
                    self.mg.round()
                with context('Mokey 0'):
                    with it('must have items 16, 18, 21, 20, 122'):
                        expect(self.mg.monkeys[0].items).to(contain_exactly(16, 18, 21, 20, 122))
                with context('Monkey 1'):
                    with it('must have items 1468, 22, 150, 286, 739'):
                        expect(self.mg.monkeys[1].items).to(contain_exactly(1468, 22, 150, 286, 739))
                with context('Monkey 2'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[2].items).to(be_empty)
                with context('Monkey 3'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[3].items).to(be_empty)
            with context('After round 20'):
                with before.all as self:
                    for _ in range(0, 17):
                        self.mg.round()
                with context('Mokey 0'):
                    with it('must have items 10, 12, 14, 26, 34'):
                        expect(self.mg.monkeys[0].items).to(contain_exactly(10, 12, 14, 26, 34))
                    with it('must have inspected items 101 times'):
                        expect(self.mg.monkeys[0].inspections).to(equal(101))
                with context('Monkey 1'):
                    with it('must have items 245, 93, 53, 199, 115'):
                        expect(self.mg.monkeys[1].items).to(contain_exactly(245, 93, 53, 199, 115))
                    with it('must have inspected items 95 times'):
                        expect(self.mg.monkeys[1].inspections).to(equal(95))
                with context('Monkey 2'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[2].items).to(be_empty)
                    with it('must have inspected items 7 times'):
                        expect(self.mg.monkeys[2].inspections).to(equal(7))
                with context('Monkey 3'):
                    with it('must have no items'):
                        expect(self.mg.monkeys[3].items).to(be_empty)
                    with it('must have inspected items 105 times'):
                        expect(self.mg.monkeys[3].inspections).to(equal(105))
                with context('monkey business'):
                    with it('must be 10605'):
                        expect(self.mg.monkey_business).to(equal(10605))
