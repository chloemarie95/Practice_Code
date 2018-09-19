import random

feet_in_mile = 5280
meters_in_km = 1000


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    '''pass in sided dice'''
    return random.randint(1, num)


############################# Multiple Choice Quiz ##########################################

question_prompts = [
    "What word describes the parameter of a tuple?\na) Mutuble\nb) Immutuble\nc) Both\n\n",
    "How can a module be imported?\na) Built-in/external\nb) Third party\nc) Both\n\n",
    "What does [:::] mean?\na) Start, stop, stepwise\nb) Start, stepwise, stop\nc) Start, pause, stop\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    '''when answered right, increment score'''
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

##################################################################################

# Inheritance - inherit attributes/functions from another class

class Chef:

    def make_soup(self):
        print("The chef made soup")

    def make_salad(self):
        print("The chef made salad")

    def make_special_dish(self):
        print("The chef made Pho")


my_chef = Chef()
my_chef.make_special_dish()


class ItalianChef(Chef): # Inherits all the functions from the previous chef class

    def make_pasta(self):
        print("The chef made pasta")

    def make_special_dish(self):
        '''can override inherited attributes'''
        print("The chef made lasange")

new_chef = ItalianChef()
new_chef.make_soup()
new_chef.make_pasta()
new_chef.make_special_dish()