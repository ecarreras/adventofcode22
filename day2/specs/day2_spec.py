from mamba import *
from expects import *
from day2.game import Game, Round, Shape, Round2


with description('With a game strategy'):
    with description('An A Y strategy'):
        with before.each as self:
            self.r = Round('A', 'Y')
        with it('openent Shape must be a Rock'):
            expect(self.r.openent_shape).to(equal(Shape.Rock))
        
        with it('my Shape must be a Paper'):
            expect(self.r.me_shape).to(equal(Shape.Paper))
        
        with it('total score must be 8'):
            expect(self.r.score).to(equal(8))

    with description('An B X strategy'):
        with before.each as self:
            self.r = Round('B', 'X')
        with it('openent Shape must be a Paper'):
            expect(self.r.openent_shape).to(equal(Shape.Paper))
        
        with it('my Shape must be a Rock'):
            expect(self.r.me_shape).to(equal(Shape.Rock))
        
        with it('total score must be 1'):
            expect(self.r.score).to(equal(1))
    
    with description('An C Z strategy'):
        with before.each as self:
            self.r = Round('C', 'Z')
        with it('openent Shape must be a Scissors'):
            expect(self.r.openent_shape).to(equal(Shape.Scissors))
        
        with it('my Shape must be a Scissors'):
            expect(self.r.me_shape).to(equal(Shape.Scissors))
        
        with it('total score must be 6'):
            expect(self.r.score).to(equal(6))
    

with description('Calculating a result of game'):
    with description('An A Y, B X, C Z strategy'):
        with it('must be a total of 15 score'):
            game = Game()
            game.add_round(Round('A', 'Y'))
            game.add_round(Round('B', 'X'))
            game.add_round(Round('C', 'Z'))
            expect(game.total).to(equal(15))


with description('Parsing a text strategy'):
    text_strategy = """
    A Y
    B X
    C Z
    """
    game = Game()
    game.add_round_from_text(text_strategy)
    expect(game.total).to(equal(15))


with description('With a game strategy2'):
    with description('An A Y strategy'):
        with before.each as self:
            self.r = Round2('A', 'Y')
        with it('openent Shape must be a Rock'):
            expect(self.r.openent_shape).to(equal(Shape.Rock))
        
        with it('my Shape must be a Rock'):
            expect(self.r.me_shape).to(equal(Shape.Rock))
        
        with it('total score must be 4'):
            expect(self.r.score).to(equal(4))
    
    with description('An B X strategy'):
        with before.each as self:
            self.r = Round2('B', 'X')
        with it('openent Shape must be a Paper'):
            expect(self.r.openent_shape).to(equal(Shape.Paper))
        
        with it('my Shape must be a Rock'):
            expect(self.r.me_shape).to(equal(Shape.Rock))
        
        with it('total score must be 1'):
            expect(self.r.score).to(equal(1))
    
    with description('An C Z strategy'):
        with before.each as self:
            self.r = Round2('C', 'Z')
        with it('openent Shape must be a Scissors'):
            expect(self.r.openent_shape).to(equal(Shape.Scissors))
        
        with it('my Shape must be a Rock'):
            expect(self.r.me_shape).to(equal(Shape.Rock))
        
        with it('total score must be 7'):
            expect(self.r.score).to(equal(7))


with description('Calculating a result of game'):
    with description('An A Y, B X, C Z strategy'):
        with it('must be a total of 15 score'):
            game = Game()
            game.add_round(Round2('A', 'Y'))
            game.add_round(Round2('B', 'X'))
            game.add_round(Round2('C', 'Z'))
            expect(game.total).to(equal(12))


with description('Parsing a text strategy'):
    text_strategy = """
    A Y
    B X
    C Z
    """
    game = Game()
    game.add_round_from_text(text_strategy, Round2)
    expect(game.total).to(equal(12))