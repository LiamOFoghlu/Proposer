from operator import mod
from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Offer'
    players_per_group = None
    num_rounds = 1
    money = "£3.00"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Offer = models.StringField(
        label = "Would you like to offer 10% or 40% of £3.00 to the receiver?",
        choices = [
            "10%",
            "40%"
        ],
        widget = widgets.RadioSelectHorizontal
    )


# PAGES

class Offer(Page):
    form_model = 'player'
    form_fields = ['Offer']

page_sequence = [Offer]
