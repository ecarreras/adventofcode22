from mamba import *
from expects import *
from day8.trees import Map, Tree


with description('Day 8'):
    with description('A map of trees'):
        with before.all as self:
            input = """
            30373
            25512
            65332
            33549
            35390
            """
            self.map = Map(input)
        with it('has 16 corners trees'):
            expect(self.map.corners_trees).to(equal(16))
        
        with it('has a matrix from length tree'):
            expect(self.map.matrix[1][1]).to(equal(5))
            expect(self.map.matrix[3][3]).to(equal(4))
        
        with context('The top-left 5'):
            with it('should be visible from the left and top'):
                visibility = self.map.is_visible(1, 1)
                expect(visibility).to(contain_exactly('left', 'top'))
        
        with context('The top-middle 5'):
            with it('should be visible from the top and right'):
                visibility = self.map.is_visible(1, 2)
                expect(visibility).to(contain_only('top', 'right'))
        
        with context('The top-right 1'):
            with it('not should be visible from any direction'):
                visibility = self.map.is_visible(1, 3)
                expect(visibility).to(be_empty)
        
        with context('The left-middle 5'):
            with it('should be visible, but only from the right'):
                visibility = self.map.is_visible(2, 1)
                expect(visibility).to(contain_only('right'))
        
        with context('The center 3'):
            with it('not should be visible from any direction'):
                visibility = self.map.is_visible(2, 2)
                expect(visibility).to(be_empty)
        
        with context('The right-middle 3'):
            with it('should be visible from the right'):
                visibility = self.map.is_visible(2, 3)
                expect(visibility).to(contain_only('right'))
        
        with context('In the bottom row'):
            with context('the middle 5'):
                with it('should be visible'):
                    visibility = self.map.is_visible(3, 2)
                    expect(bool(visibility)).to(be_true)
            with context('but the 3 and 4'):
                with it('should not be visible'):
                    visibility = self.map.is_visible(3, 1)
                    expect(bool(visibility)).to(be_false)
                    visibility = self.map.is_visible(3, 3)
                    expect(bool(visibility)).to(be_false)
        
        with description('Counting a total of visibles trees'):
            with it('should be 21'):
                expect(self.map.visible_trees).to(equal(21))
        
        with description('Calculating the score of a tree'):
            with context('The middle 5 in the second row'):
                with before.all as self:
                    self.t = Tree((1, 2), self.map.matrix)
                    self.t.score

                with it('must see 1 tree on top'):
                    expect(self.t.num_trees['top']).to(equal(1))
                with it('must see 1 tree on left'):
                    expect(self.t.num_trees['left']).to(equal(1))
                with it('must see 2 tree on right'):
                    expect(self.t.num_trees['right']).to(equal(2))
                with it('must see 2 tree on down'):
                    expect(self.t.num_trees['bottom']).to(equal(2))
                
                with it('should have a score of 4'):
                    expect(self.t.score).to(equal(4))
        
        with description('Calculating the max score of the map'):
            with it('should be 8'):
                expect(self.map.max_score).to(equal(8))