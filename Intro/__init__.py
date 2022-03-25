from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1
    compensation = "£1.00"
    money = "£3.00"
    offers = (0.4, 0.1)
    max_payoff = "£" + str(round(float(money[1:4]) - offers[1]*float(money[1:4]), 2))
    if len(max_payoff) == 4:
        max_payoff = max_payoff + "0"


class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    import random
    for player in subsession.get_players():         # iterate through the players
        prob = random.uniform(0,1)
        if prob < 0.6667:
            player.participant.proposer_ball = 0
            player.Merit = "non-earner"
        else:
            player.participant.proposer_ball = 1
            player.Merit = "earner"

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ProlificID = models.StringField()
    Merit = models.StringField()
    start_epochtime = models.IntegerField()
    start_clocktime = models.StringField()


# PAGES
class Consent(Page):
    def is_displayed(player):
        # record time player entered application
        import time 
        time_in = round(time.time())
        player.start_epochtime = time_in
        player.participant.start_epochtime = time_in
        player.start_clocktime = time.strftime('%H:%M:%S', time.localtime(time_in))
        return 1

class ProlificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']


class Instructions(Page):
    pass

class Draw(Page):  
    def vars_for_template(player):
        if player.participant.proposer_ball == 1:
            template = "Intro/Draw_Task.txt" 
        else:
            template = "Intro/Draw_No_Task.txt"
        return dict(
            template = template,
        )
    def app_after_this_page(player, upcoming_apps):
        if player.participant.proposer_ball == 0:
            return upcoming_apps[1]        # upcoming_apps is a list containing the remaining apps defined in the app_sequenc in the settings.py SESSSION_CONFIGS. upcoming_apps[0] is the next app (maths task); upcoming_apps[1] is the one after that (offer). This function skips to the Offer if the player drew an N ball.


page_sequence = [Consent, ProlificID, Instructions, Draw]
