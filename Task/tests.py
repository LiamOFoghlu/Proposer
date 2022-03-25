from otree.api import *
from Task import Results, Task


class PlayerBot(Bot):
    def play_round(self):

        if self.player.participant.proposer_ball == 0:
            pass 
        else:
            # Task
            yield Task, dict(q1 = "14", q2 = "(x - 3)(3y - 2)", q3 = "10.50", q4 = "50%")
            
            # Results
            yield Results

