from mamba import *
from expects import *
from day4.cleanup import Assignment, AssignmentProcessor


with description('Day 4'):
    with description('An assignment pairs'):
        with description('Assignment 2-4,6-8'):
            with before.each as self:
                self.a = Assignment('2-4,6-8')
            with context('the first elf'):
                with it('should be assigned to 2,3,4'):
                    expect(self.a.assignments[0]).to(contain_exactly(2, 3, 4))
            with context('the second elf'):
                with it('should be assigned to 6,7,8'):
                    expect(self.a.assignments[1]).to(contain_exactly(6, 7, 8))
            with it('should not assignment is duplicated'):
                expect(self.a.is_contained).to(be_false)
            with it('should not overlap'):
                expect(self.a.overlaps).to(be_false)

        with description('Assignment 2-8,3-7'):
            with before.each as self:
                self.a = Assignment('2-8,3-7')
            with context('the first elf'):
                with it('should be assigned to 2,3,4,5,6,7,8'):
                    expect(self.a.assignments[0]).to(contain_exactly(2, 3, 4, 5, 6, 7, 8))
            with context('the second elf'):
                with it('should be assigned to 3,4,5,6,7'):
                    expect(self.a.assignments[1]).to(contain_exactly(3, 4, 5, 6, 7))
            with it('should assignment duplicated'):
                expect(self.a.is_contained).to(be_true)
            with it('should overlap'):
                expect(self.a.overlaps).to(be_true)
    
    with description('An assignment processor'):
        with before.each as self:
            input = """
            2-4,6-8
            2-3,4-5
            5-7,7-9
            2-8,3-7
            6-6,4-6
            2-6,4-8
            """
            self.ap = AssignmentProcessor(input)
        with it('should detect 2 contained'):
            expect(self.ap.number_of_contained).to(equal(2))
        with it('should detect 4 overlaps'):
            expect(self.ap.number_of_overlaps).to(equal(4))
