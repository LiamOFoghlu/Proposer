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
        label = "A shop has an offer: buy 8 kiwis, and every extra kiwi after that is half price. A man goes to the shop and pays £5.50 for some kiwis. The full price of a kiwi is £0.50. How many does he buy?",
        choices = [
            "14",
            "12",
            "10",
            "15"
        ],
        widget = widgets.RadioSelectHorizontal
    ) 
    q2 = models.StringField(
        label = "Which of the following is equal to 3y(x - 3) - 2(x - 3)?",
        choices = [
            "3y(x - 3)",
            "(x - 3)(3y - 2)",
            "2y(x - 3)",
            "(x - 3)(x - 3)"
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
        label = "A trader takes a loan of £120, with 5 percent interest. They buy a painting for £120 and sell it for £189. The profit expressed as a percentage of total cost, including interest, is:",
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
        timeout_seconds = 8*60
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
        if player.q1 == "14":
            correct_answers = correct_answers + 1
        if player.q2 == "(x - 3)(3y - 2)":
            correct_answers = correct_answers + 1       
        if player.q3 == "10.50":
            correct_answers = correct_answers + 1 
        if player.q4 == "50%":
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
