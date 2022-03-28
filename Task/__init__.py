from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Task'
    players_per_group = None
    num_rounds = 1
    money = "£3.00"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(
        label = "A shop has an offer: buy 8 kiwis, and every extra kiwi after that is half price. A man goes to the shop and pays £4.50 for some kiwis. The full price of a kiwi is £0.50. How many does he buy?",
        choices = [
            "9",
            "12",
            "10",
            "15"
        ],
        widget = widgets.RadioSelectHorizontal
    ) 
    q2 = models.StringField(
        label = "A hairdresser has an offer: every third visit is free. They charge £48 for a haircut. Last year Sarah paid £144 for a haaircut. How many times did she go?",
        choices = [
            "Two times",
            "Three times",
            "Four times",
            "Five times"
        ],
        widget = widgets.RadioSelectHorizontal
    )     
    q3 = models.StringField(
        label = "A woman walks from the bottom to the top of a hill. She starts at 9.40am and arrives at the top at 10.20 am. She takes a rest for ten minutes. Then she walks back down. On the way down she walks twice as fast as she did on the way up. What time is it when she reaches the bottom of the hill?",
        choices = [
            "11.20",
            "10.40",
            "10.50",
            "11.10"
        ],
        widget = widgets.RadioSelectHorizontal
    )   
    q4 = models.StringField(
        label = "A trader buys a painting for £120 and sells it for £170. They pay a £10 transaction fee. Their profit expressed as a percentage of total cost is:",
        choices = [
            "50%",
            "60%",
            "80%",
            "33%"
        ],
        widget = widgets.RadioSelectHorizontal
    )     
    timeout_occured = models.BooleanField()
    correct_answers = models.IntegerField()
    task_failed = models.BooleanField()


# PAGES
class Task(Page):
    form_model = 'player'

    def get_timeout_seconds(player):
        timeout_seconds = 6*60
        return timeout_seconds    

    form_fields = [
        'q1',
        'q2',
        'q3',
        'q4'
    ]

    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.timeout_occured = True
        
        # tot up correct answers
        correct_answers = 0
        if player.q1 == "10":
            correct_answers = correct_answers + 1
        if player.q2 == "Four times":
            correct_answers = correct_answers + 1       
        if player.q3 == "10.50":
            correct_answers = correct_answers + 1 
        if player.q4 == "33%":
            correct_answers = correct_answers + 1  
        player.correct_answers = correct_answers
        if correct_answers < 3:
            player.task_failed = True
        else:
            player.task_failed = False

class Results(Page):
    def vars_for_template(player):
        if player.correct_answers >= 3:
            template = "Task/Task_Success.txt" 
        else:
            template = "Task/Task_Fail.txt"
        return dict(
            template = template,
        ) 

    def app_after_this_page(player, upcoming_apps):
        if player.correct_answers < 3:
            return upcoming_apps[1]        # upcoming_apps is a list containing the remaining apps defined in the app_sequenc in the settings.py SESSSION_CONFIGS. upcoming_apps[0] is the next app (offer); upcoming_apps[1] is the one after that (debrief). This function skips the Offer if the player fails the task.


page_sequence = [Task, Results]
