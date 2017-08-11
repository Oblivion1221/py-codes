import random


def easy_level(lst):
    choice_list = []
    [choice_list.append(c) for c in lst if type(c) is int]
    return random.choice(choice_list)
