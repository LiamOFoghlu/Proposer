from otree.api import *

from Offer import Offer


class PlayerBot(Bot):
    def play_round(self):

        import random
        prob = random.uniform(0,1)
        if prob < 0.25:
            low = True 
        else:
            low = False 
        if low:
            yield Offer, dict(Offer = "10%")
        else:
            yield Offer, dict(Offer = "40%")