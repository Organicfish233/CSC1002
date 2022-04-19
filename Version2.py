from random import randint

g_game_round = 0 #Count the game rounds.
g_guess_time = 0 #Count the times of guess.
g_scale_use_time = 0 #Count the times of using the scale.

greeting = """Welcome to the Odd Ball Game.
You are going to choose several balls, in which hides an odd ball.
The odd ball looks the same as other balls, but it's a little bit heavier.
You are provide with a scale to find out the odd ball.
Good Luck to You!
"""


# Randomly select an odd ball.
def choose_odd_ball(p_number_of_balls):
    index = randint(1,int(p_number_of_balls))
    return index


# Prompt the user to input the number of balls.
def input_number_of_balls():
    result = input("Please input the number of balls. \
It should be a positive even integer.\nInput here:")
    return result


# Prompt the user to input the identifiers of several balls.
# There balls will be put on either side of the scale.
# More than one spaces between the identifiers are allowed.
def input_identifier_of_balls(p_side):
    result = input("Please input the identifiers of the ball(s) \
to be placed on the %s pan: "% p_side)
    return result.split()


# Prompt the user to guess the identifier of the odd ball.
def input_guess():
    guess = input("Please guess the identifier of the odd ball. \
You can directly press Enter to proceed to reweighing. \nInput here:")
    return guess


# Check whether the number of balls is valid.
# If not, raise an error to be catched later.
# Invalid Situation: not a non-negative integer; an odd number; equal to 0.
def check_number_validity(p_user_input):
    if not p_user_input.isdigit():
        raise ValueError("The input '%s' \
is not a positive integer."% p_user_input)
    elif eval(p_user_input)%2 != 0:
        raise ValueError("The input '%s' is not even."% p_user_input)
    elif eval(p_user_input) == 0:
        raise ValueError("The input '%s' is not larger than 0." %p_user_input)


# Check whether the identifiers of the balls are all valid.
# If not, raise an error to be catched later.
# Invalid situation: no identifier is input; not a non-negative integer; 
# Invalid situation: equal to 0; larger than the maximum number.
def check_identifier_validity(p_user_input,p_number_of_balls):
    if p_user_input == []:
        raise ValueError("Please at least put one ball on the scale.")
    for i in p_user_input:
        if not i.isdigit():
            raise ValueError("The input '%s' is not a positive integer."% i)
        elif eval(i) == 0:
            raise ValueError("The input '%s' is not larger than 0." %i)
        elif eval(i) > p_number_of_balls:
            raise IndexError("The input '%s' is out of range. \
You have only %d balls."%(i,p_number_of_balls))


# Check whether a single ball is placed on both sides.
# If it is, raise an error to be catched later.
# Invalid situation: The same ball appear in both sides; 
# Invalid situation: the numbers of balls on the both sides are not eauql.
def check_both_sides(p_left_balls,p_right_balls):
    for ball in p_left_balls:
        if ball in p_right_balls:
            raise ValueError("The ball '%s' appear in both \
sides of the scale."% ball)
    if len(p_left_balls) != len(p_right_balls):
        raise ValueError("The numbers of the balls on both sides are not equal.")


# Check whether the guess of user is valid.
# If not, raise an error to be catched later.
# An empty input is acceptable.
# Invalid situation: not a non-negative integer.
# Invalid situation: equal to 0; larger than the maximum number.
def check_guess_validity(p_guess,p_number_of_balls):
    if p_guess == "":
        pass
    elif not p_guess.isdigit():
        raise ValueError("Your guess '%s' is not a positive integer."% p_guess)
    elif eval(p_guess) == 0:
        raise ValueError("Your guess '%s' is not larger than 0."% p_guess)
    elif eval(p_guess) > p_number_of_balls:
        raise IndexError("Your guess '%s' is out of range. \
You only have %d balls."% (p_guess,p_number_of_balls))


# Ask the user to input the number of balls. 
# Warn the user when the input is invalid, then ask him to try again.
def prompt_input_number():
    while True:
        user_input = input_number_of_balls()
        try:
            check_number_validity(user_input)
            break
        except BaseException as e:
            print(e)
            print("Please try again.\n")
            continue
    return user_input


# Ask the user to input the identifiers of the balls. 
# Warn the user when the input is invalid, then ask him to try again.
def prompt_input_identifier(p_side,p_number_of_balls):
    while True:
        identifier_list = input_identifier_of_balls(p_side)
        try:
            check_identifier_validity(identifier_list,p_number_of_balls)
            break
        except BaseException as e:
            print(e)
            print("Please try again.\n")
            continue
    return identifier_list


# Ask the user to select the balls to be placed on the left or the right. 
# Warn the user when the input is invalid, then ask him to try again.
def prompt_input_bothsides(p_number_of_balls):
    while True:
        left_balls = prompt_input_identifier("left",p_number_of_balls)
        right_balls = prompt_input_identifier("right",p_number_of_balls)
        try:
            check_both_sides(left_balls,right_balls)
            break
        except BaseException as e:
            print(e)
            print("Please choose the balls again.\n")
            continue
    return left_balls,right_balls


# Ask the user to guess the identifier of the odd ball.
# Warn the user when the input is invalid, then ask him to try again.
def prompt_guess(p_number_of_balls):
    while True:
        guess = input_guess()
        try:
            check_guess_validity(guess,p_number_of_balls)
            break
        except BaseException as e:
            print(e)
            print("Please try again.")
            continue
    return guess


def weigh(p_left_balls,p_right_balls,OddIndex):
    if str(OddIndex) in p_left_balls:
        result = "Left Heavier"
    elif str(OddIndex) in p_right_balls:
        result = "Right Heavier"
    else:
        result = "Balanced!"
    return result


# Demonstrate the inputs of the user.
def demonstrate(p_left_balls,p_right_balls):
    print("Your inputs for left: ",end = " ")
    for i in p_left_balls:
        print(i,end = " ")
    print()
    print("Your inputs for right:",end = " ")
    for i in p_right_balls:
        print(i,end = " ")
    print()


def check_guess_correctness(p_index_of_oddball,p_guess):
    global g_guess_time
    if p_guess == "":
        g_guess_time -= 1
        raise ValueError("You choose to skip the guessing chance and reweigh.")
    elif not p_index_of_oddball == int(p_guess):
        raise ValueError("Sorry, your guess is wrong.")


# One round of the game.
def start_one_round(p_number_of_balls,p_identifier_of_oddball):
    global g_guess_time
    global g_scale_use_time
    print()
    print("Next, please input the identifiers of the balls \
you want to put on the scale. \
The identifiers are in consecutive numerical sequence, starting with 1. \
The identifiers should be positive numbers separated by a minimum space. \
e.g. 1 2 11\n")
    left_balls,right_balls = prompt_input_bothsides(p_number_of_balls)
    demonstrate(left_balls,right_balls)
    print(weigh(left_balls,right_balls,p_identifier_of_oddball))
    user_guess = prompt_guess(p_number_of_balls)
    g_guess_time += 1
    g_scale_use_time += 1
    try:
        check_guess_correctness(p_identifier_of_oddball,user_guess)
        return True
    except BaseException as e:
        print(e)
        print("Please select the balls and then guess again...")
        return False


# The loop is the main process of the game.
# The loop breaks only when the user successfully find the odd ball.
def game_loop():
    global g_guess_time
    global g_game_round
    global g_scale_use_time
    number_of_balls = int(prompt_input_number())
    identifier_of_oddball = choose_odd_ball(number_of_balls)
    g_game_round += 1
    while True:
        if start_one_round(number_of_balls,identifier_of_oddball) == True:
            print("Congratulations, your guess is correct!")
            print("You've guessed %d time(s)."% g_guess_time)
            print("You've used the scale for %d time(s)." % g_scale_use_time)
            g_guess_time = 0
            g_scale_use_time = 0
            break


# The loop of different rounds of the game.
# The user can choose to quit after each round.
print(greeting)
while True:
    game_loop()
    print("Round %d ends. Would you like to start a new round?"% g_game_round)
    print("Input yes to start a new round, otherwise to quit.")
    user_choice = input("Input here:")
    if user_choice == "yes":
        print("------------------------")
        print("Round %d starts..."% (g_game_round+1))
        continue
    else:
        break


