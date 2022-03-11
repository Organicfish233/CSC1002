from random import randint

g_game_round = 0
g_guess_time = 0

# Randomly select an odd ball.
def choose_odd_ball(NumberOfBalls):
    index = randint(0,int(NumberOfBalls))
    return index


# Prompt the user to input the number of balls.
def input_number_of_balls():
    result = input("Please input the number of balls. It should be a positive even integer.\nInput here:")
    return result


# Prompt the user to input the identifiers of several balls.
# There balls will be put on either side of the scale.
def input_identifier_of_balls(side):
    result = input("""Please input the identifiers of the balls you want to put on the %s side of the scale.
The identifiers should be positive numbers separated by a minimum space. e.g. 1 2 11\nInput here:""" %side)
    return result.split(" ")


# Prompt the user to guess the identifier of the odd ball.
def input_guess():
    guess = input("Please guess the identifier of the odd ball.\nInput here:")
    return guess


# Check whether the number of balls is valid, if not, raise an error to be catched later.
def check_number_validity(UserInput):
    if not UserInput.isdigit():
        raise ValueError("The input %s is not a positive integer."% UserInput)
    elif eval(UserInput)%2 != 0:
        raise ValueError("The input %s is not even."% UserInput)
    elif eval(UserInput) == 0:
        raise ValueError("The input %s is not larger than 0." %UserInput)


# Check whether the identifiers of the balls are all valid, if not, raise an error to be catched later.
def check_identifier_validity(UserInput,NumberOfBalls):
    for i in UserInput:
        if not i.isdigit():
            raise ValueError("The input %s is not a positive integer."% UserInput)
        elif eval(i) == 0:
            raise ValueError("The input %s is not larger than 0." %UserInput)
        elif eval(i) > NumberOfBalls:
            raise IndexError("The input %s is out of range. You have only %d balls."%(i,NumberOfBalls))


# Check whether a single ball is placed on both sides, if it is, raise an error to be catched later.
def check_both_sides(LeftBalls,RightBalls):
    for ball in LeftBalls:
        if ball in RightBalls:
            raise ValueError("The ball %s appear in both sides of the scale."% ball)


# Check whether the guess of user is valid, if not, raise an error to be catched later.
def check_guess_validity(Guess,NumberOfBalls):
    if not Guess.isdigit():
        raise ValueError("Your guess %s is not a positive integer."% Guess)
    elif eval(Guess) == 0:
        raise ValueError("Your guess %s is not larger than 0."% Guess)
    elif eval(Guess) > NumberOfBalls:
        raise IndexError("Your guess %s is out of range. You only have %d balls."% (Guess,NumberOfBalls))


# Ask the user to input the number of balls. 
# Alert the user if the input is invalid, then ask him to try again.
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
# Alert the user if the input is invalid, then ask him to try again.
def prompt_input_identifier(side,NumberOfBalls):
    while True:
        identifier_list = input_identifier_of_balls(side)
        try:
            check_identifier_validity(identifier_list,NumberOfBalls)
            break
        except BaseException as e:
            print(e)
            print("Please try again.\n")
            continue
    return identifier_list


# Ask the user to select the balls to be placed on the left or the right. 
# Alert the user if the input is invalid, then ask him to try again.
def prompt_input_bothsides(NumberOfBalls):
    while True:
        left_balls = prompt_input_identifier("left",NumberOfBalls)
        right_balls = prompt_input_identifier("right",NumberOfBalls)
        try:
            check_both_sides(left_balls,right_balls)
            break
        except BaseException as e:
            print(e)
            print("Please choose the balls again.\n")
            continue
    return left_balls,right_balls


# Ask the user to guess the identifier of the odd ball.
# Alert the user if the input is invalid, then ask him to try again.
def prompt_guess(NumberOfBalls):
    while True:
        guess = input_guess()
        try:
            check_guess_validity(guess,NumberOfBalls)
            break
        except BaseException as e:
            print(e)
            print("Please try again.")
            continue
    return guess


# Weigh the balls.
def weigh(LeftBalls,RightBalls,OddIndex):
    if len(LeftBalls) > len(RightBalls):
        result = "Left Heavier"
    elif len(LeftBalls) < len(RightBalls):
        result = "Right Heavier"
    elif str(OddIndex) in LeftBalls:
        result = "Left Heavier"
    elif str(OddIndex) in RightBalls:
        result = "Right Heavier"
    else:
        result = "Balanced!"
    return result


def check_guess_correctness(IndexOfOddball,Guess):
    if not IndexOfOddball == Guess:
        raise ValueError("Sorry, your guess is wrong.")


# One round of the game.
def start_one_round(number_of_balls,identifier_of_oddball):
    global g_game_round
    global g_guess_time
    g_game_round += 1
    left_balls,right_balls = prompt_input_bothsides(number_of_balls)
    print(weigh(left_balls,right_balls,identifier_of_oddball))
    user_guess = int(prompt_guess(number_of_balls))
    g_guess_time += 1
    try:
        check_guess_correctness(identifier_of_oddball,user_guess)
        return True
    except BaseException as e:
        print(e)
        print("Please select the balls and then guess again...")
        return False


# The game loop. The loop breaks only when the user successfully find the odd ball.
def game_loop():
    global g_guess_time
    number_of_balls = int(prompt_input_number())
    identifier_of_oddball = choose_odd_ball(number_of_balls)
    while True:
        if start_one_round(number_of_balls,identifier_of_oddball) == True:
            print("Congratulations, your guess is correct!")
            print("You've guessed %d time(s)."% g_guess_time)
            g_guess_time = 0
            break


# The loop of different rounds of the game.
# The user can choose to quit after each round.
while True:
    game_loop()
    print("Round %d ends. Would you like to start a new round?"% g_game_round)
    print("Input yes to start a new round, otherwise quit.")
    user_choice = input("Input here:")
    if user_choice == "yes":
        print("------------------")
        print("Round %d starts..."% (g_game_round+1))
        continue
    else:
        break


