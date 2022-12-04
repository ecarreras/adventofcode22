from mamba import *
from expects import *
from day3.rucksack import Rucksack, RuckSacksProcessor, RucksackGroup


with description('Day 3'):
    with description('A Rucksack'):
        with description('with list of components vJrwpWtwJgWrhcsFMMfFFhFp'):
            with before.each as self:
                self.rucksack = Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')
            with it('has contain vJrwpWtwJgWr in the first compartment'):
                expect(self.rucksack.compartments[0]).to(equal('vJrwpWtwJgWr'))
            with it('has contain vJrwpWtwJgWr in the first compartment'):
                expect(self.rucksack.compartments[1]).to(equal('hcsFMMfFFhFp'))
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('p'))
            with it('has a priority of 16'):
                expect(self.rucksack.priority).to(equal(16))
        
        with description('with list of components jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'):
            with before.each as self:
                self.rucksack = Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
            with it('has contain jqHRNqRjqzjGDLGL in the first compartment'):
                expect(self.rucksack.compartments[0]).to(equal('jqHRNqRjqzjGDLGL'))
            with it('has contain rsFMfFZSrLrFZsSL in the first compartment'):
                expect(self.rucksack.compartments[1]).to(equal('rsFMfFZSrLrFZsSL'))
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('L'))
            with it('has a priority of 38'):
                expect(self.rucksack.priority).to(equal(38))
        
        with description('with list of components PmmdzqPrVvPwwTWBwg'):
            with before.each as self:
                self.rucksack = Rucksack('PmmdzqPrVvPwwTWBwg')
            with it('has contain PmmdzqPrV in the first compartment'):
                expect(self.rucksack.compartments[0]).to(equal('PmmdzqPrV'))
            with it('has contain vPwwTWBwg in the first compartment'):
                expect(self.rucksack.compartments[1]).to(equal('vPwwTWBwg'))
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('P'))
            with it('has a priority of 42'):
                expect(self.rucksack.priority).to(equal(42))
        

        with description('with list of components wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'):
            with before.each as self:
                self.rucksack = Rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('v'))
            with it('has a priority of 22'):
                expect(self.rucksack.priority).to(equal(22))

        with description('with list of components ttgJtRGJQctTZtZT'):
            with before.each as self:
                self.rucksack = Rucksack('ttgJtRGJQctTZtZT')
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('t'))
            with it('has a priority of 20'):
                expect(self.rucksack.priority).to(equal(20))
        
        with description('with list of components CrZsJsPPZsGzwwsLwLmpwMDw'):
            with before.each as self:
                self.rucksack = Rucksack('CrZsJsPPZsGzwwsLwLmpwMDw')
            with it('has to detect p as duplicated in two compartments'):
                expect(self.rucksack.errors).to(contain_exactly('s'))
            with it('has a priority of 19'):
                expect(self.rucksack.priority).to(equal(19))
    
    with description('A Priority'):
        with it('priorty of a is 1 and z is 26'):
            expect(Rucksack.get_priority('a')).to(equal(1))
            expect(Rucksack.get_priority('z')).to(equal(26))
        
        with it('priorty of A is 27 and Z is 52'):
            expect(Rucksack.get_priority('A')).to(equal(27))
            expect(Rucksack.get_priority('Z')).to(equal(52))
    

    with description('All the Rucksacks'):
        with before.each:
            items = """
            vJrwpWtwJgWrhcsFMMfFFhFp
            jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
            PmmdzqPrVvPwwTWBwg
            wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
            ttgJtRGJQctTZtZT
            CrZsJsPPZsGzwwsLwLmpwMDw
            """
            self.rp = RuckSacksProcessor(items)
        with it('should have a 157 of prioriy'):
            expect(self.rp.total_priority).to(equal(157))
        with it('should have two groups'):
            expect(self.rp.groups).to(have_len(2))
        with it('should get a group priority of 70'):
            expect(self.rp.group_priority).to(equal(70))
    
    with description('A group of rucksacks'):
        with description('the first group'):
            with before.each as self:
                r1 = Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')
                r2 = Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
                r3 = Rucksack('PmmdzqPrVvPwwTWBwg')
                self.rg = RucksackGroup([r1, r2, r3])
            with it('must have the r badge'):
                expect(self.rg.badge).to(equal('r'))
            with it('must have priority of 18'):
                expect(self.rg.priority).to(equal(18))

        
        with description('the second group'):
            with before.each as self:
                r1 = Rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
                r2 = Rucksack('ttgJtRGJQctTZtZT')
                r3 = Rucksack('CrZsJsPPZsGzwwsLwLmpwMDw')
                self.rg = RucksackGroup([r1, r2, r3])
            with it('must have the r badge'):
                expect(self.rg.badge).to(equal('Z'))
            with it('must have priority of 52'):
                expect(self.rg.priority).to(equal(52))
