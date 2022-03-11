from random import randint
g_GuessTime = 0  # The number of guess times in a single round.

# Prompt the user to enter the identifies of the balls he want to select.
# Parameter:The side of the; The total number of balls in this game.
# Return Value: A list including all the identifiers of the selected balls, e.g. [1,2,3].
# Exception: The function will ask the user to try to enter again if the input is invalid.
def select_balls(side,NumberOfBalls):
    pass

# Final check of the validity of the input, i.e. if some of the balls are selected more than once.
# Parameter: The total number of balls in this game
# Return Value: the identifier of the balls on the left and right pans, wrapped in a two-element tuple.
# Exception: If the input is invalid, the user will be asked to select balls again.
def final_select(NumberOfBalls):
    while True:
        left = select_balls("left",NumberOfBalls)
        right = select_balls("right",NumberOfBalls)
        if len(list(set(left).intersection(set(right)))) != 0:
            print("Some ball(s) is(are) selected more than once. Please select them again.")
            print("")
        else:
            break
    return left,right

# Produce the result of weighing.
# Parameter: The identifiers of the balls on the left and right pans respectively, and the index of the odd ball.
# Return value: No return value.
# Output: Left heavier, right heavier or balanced.
def weigh(left,right,IndexOfOddBall):
        if len(left) != len(right):
            if len(left)>len(right):
                print("Left Heavier")
                return
            else:
                print("Right Heavier")
                return
        else:
            if IndexOfOddBall in left:
                print("Left Heavier")
                return
            elif IndexOfOddBall in right:
                print("Right Heavier")
                return
            else:
                print("Balanced!")
                return

# The main body of the game.
def run_game_body():
    global g_GuessTime
    # Prompt the user to enter the number of balls.
    NumberOfBalls = input("Please enter the number of balls(It shuold be an even number):")
    while True:
        if NumberOfBalls.isdigit():
            if eval(NumberOfBalls) > 1 and eval(NumberOfBalls)%2 == 0:
                break
        print("Invalid Input! A positive even number is required.")
        NumberOfBalls = input("Please input the number of balls again:")
    NumberOfBalls = int(NumberOfBalls)
    IndexOfOddBall = randint(1,NumberOfBalls)
    while True:
        LeftBalls,RightBalls = final_select(NumberOfBalls)
        weigh(LeftBalls,RightBalls,IndexOfOddBall)
        g_GuessTime += 1
        while True:
            GuessIndex = input("Please guess the identifier of the odd ball: ")
            if GuessIndex.isdigit():
                if int(GuessIndex) == float(GuessIndex) and int(GuessIndex) > 0 and int(GuessIndex) <= NumberOfBalls:
                    break
            print("Invalid Input! An integer smaller than the number of balls is required. Please try again.")
        GuessIndex = int(GuessIndex)
        if GuessIndex == IndexOfOddBall:
            print("Congratulations! You find the odd ball.")
            break
        else:
            print("Sorry, your guess is wrong. Please try again.")
            print("")

while True:
    run_game_body()
    print("Your number of guesses is: %d " %g_GuessTime)
    g_GuessTime = 0
    print("Game ends. Start a new round or quit?")
    # Prompt the user to choose whether to start a new game.
    choice = input("Input 'new' if you want to start new game. If you want to quit, please any other word.\n")
    if choice == "new":
        print("---------------------------")
        print("Start a new round...")
        continue
    else:
        print("You choose to quit.")
        quit()
