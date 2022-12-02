from enum import Enum


class Shape:
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome:
    Lost = 0
    Draw = 3
    Won = 6


LETTERS_MAP = {
    'A': Shape.Rock,
    'Y': Shape.Paper,
    'B': Shape.Paper,
    'X': Shape.Rock,
    'C': Shape.Scissors,
    'Z': Shape.Scissors
}


class Round:
    def __init__(self, oponenent, me):
        self.openent_shape = LETTERS_MAP[oponenent]
        self.me_shape = LETTERS_MAP[me]

    @property
    def score(self):
        return self.me_shape + self.outcome
    
    @property
    def outcome(self):
        if self.me_shape == self.openent_shape:
            return Outcome.Draw
        elif self.me_shape == Shape.Rock:
            if self.openent_shape == Shape.Scissors:
                return Outcome.Won
            else:
                return Outcome.Lost
        elif self.me_shape == Shape.Scissors:
            if self.openent_shape == Shape.Paper:
                return Outcome.Won
            else:
                return Outcome.Lost
        elif self.me_shape == Shape.Paper:
            if self.openent_shape == Shape.Rock:
                return Outcome.Won
            else:
                return Outcome.Lost



class Round2(Round):

  actions = {
    'X': Outcome.Lost,
    'Y': Outcome.Draw,
    'Z': Outcome.Won
  }

  def __init__(self, oponent, me):
      self.needs_to_end = self.actions[me]
      super().__init__(oponent, me)
      if self.needs_to_end == Outcome.Draw:
          self.me_shape = self.openent_shape
      elif self.needs_to_end == Outcome.Lost:
          if self.openent_shape == Shape.Paper:
              self.me_shape = Shape.Rock
          elif self.openent_shape == Shape.Scissors:
              self.me_shape = Shape.Paper
          elif self.openent_shape == Shape.Rock:
              self.me_shape = Shape.Scissors
      elif self.needs_to_end == Outcome.Won:
          if self.openent_shape == Shape.Scissors:
              self.me_shape = Shape.Rock
          elif self.openent_shape == Shape.Rock:
              self.me_shape = Shape.Paper
          elif self.openent_shape == Shape.Paper:
              self.me_shape = Shape.Scissors


class Game:
    def __init__(self) -> None:
        self.rounds = []
    
    def add_round(self, round) -> None:
        self.rounds.append(round)
    
    def add_round_from_text(self, text, round_class=Round):
        for line in text.strip().split('\n'):
            oponenent, me = line.strip().split()
            self.add_round(round_class(oponenent, me))
    
    @property
    def total(self) -> int:
        return sum(r.score for r in self.rounds)
