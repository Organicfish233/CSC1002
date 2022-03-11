from random import randint
def input_number_of_balls(*args):
    result = input("Please input the number of balls. It should be a positive even integer.\nInput here:")
    return result
def check_number_validity(user_input,*args):
    if not user_input.isdigit():
        raise ValueError("The input %s is not a positive integer."% user_input)
    elif eval(user_input)%2 != 0:
        raise ValueError("The input %s is not even."% user_input)
    elif eval(user_input) == 0:
        raise ValueError("The input %s is not larger than 0." %user_input)

def input_identifier_of_balls(side):
    result = input("""Please input the identifiers of the balls you want to put on the %s side of the scale.
The identifiers should be positive numbers separated by a minimum space. e.g. 1 2 11\nInput here:""" %side)
    return result.split(" ")

def check_identifier_validity(user_input,*args):
    for i in user_input:
        if not i.isdigit():
            raise ValueError("The input %s is not a positive integer."% user_input)
        elif eval(i) == 0:
            raise ValueError("The input %s is not larger than 0." %user_input)
        elif eval(i) > number_of_balls:
            raise IndexError("The input %s is out of range. You have only %d balls."%(i,number_of_balls))

def prompt_input(input_function,check_function,*args):
    while True:
        user_input = input_function(args[0])
        try:
            check_function(user_input)
            break
        except BaseException as e:
            print(e)
            continue
    return user_input
def start_game():
    number_of_balls = int(prompt_input(input_number_of_balls,check_number_validity,"None"))
    odd_identifier = randint(1,number_of_balls)
    left_identifier_list = prompt_input(input_identifier_of_balls,check_identifier_validity,"left")
    right_identifier_list = prompt_input(input_identifier_of_balls,check_identifier_validity,"right")
start_game()