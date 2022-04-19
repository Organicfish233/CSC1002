import turtle as tt
from random import randint
import math

# Some parameters and basic data.
g_board =[]  # 2-dimensional list to store the information of the board
g_size_of_square = 80  # The size of each square, in pixels
g_relative_size_of_gap = 0.1  # Size of gap between squares/Size of square
g_width_of_border = 5  # In pixels 
g_current = (-1,-1)  # Store the position of currently chosen square
bgcolor = (205,176,129)  # The RGB of background color
g_screen = tt.Screen()
g_status = False  # Whether the user is able to choose a color to flip
colors = {0:(248,232,208),1:(127,173,170),
2:(167,136,174),3:(216,147,164),4:(75,116,180)}  # The colors to be used
g_gap = g_relative_size_of_gap*g_size_of_square  # Size of gap
g_relative_size_of_delta = 1+g_relative_size_of_gap  # Relative size of gap plus square
g_delta = g_relative_size_of_delta*g_size_of_square  # Size of gap plus square

# Some basic settings.
tt.tracer(0)
tt.colormode(255)
tt.bgcolor(bgcolor)
tt.hideturtle() 


# Initialize the board information.
# The information will be stored in g_board.
def init_board_info():
    for i in range(5):
        g_board.append([])
        for j in range(5):
            random_number = randint(0,4)
            g_board[i].append([random_number,None,False])


# Draw a square with given size.
def draw_square(size,width):
    tt.pensize(width)
    for i in range(4):
        tt.forward(size)
        tt.left(90)
    g_screen.update()


# Draw the boundary of a square.
def draw_empty_square(
    startx,starty,
    size=g_size_of_square,width=g_width_of_border):
    tt.up()
    tt.setpos(startx,starty)
    tt.down()
    draw_square(size,width)


# Draw a square filled with color and create corresponding objects.
# Return the object.
def draw_colored_square(indexx,indexy,size,col):
    current_square = tt.Turtle()
    current_square.penup()
    current_square.turtlesize(2.7*size/60)
    current_square.shape("square")
    current_square.color(col)
    current_square.setpos(\
        g_relative_size_of_delta*(indexx-2)*g_size_of_square,
        g_relative_size_of_delta*(-indexy+2)*g_size_of_square)
    g_screen.update()
    return current_square
    

# Erase the boundary of a square.
def clear_square(indexx,indexy,size=g_size_of_square,width=g_width_of_border):
    tt.pencolor(bgcolor)
    tt.up()
    tt.setpos(get_position(indexx,indexy))
    tt.down()
    draw_square(size,width)
    tt.pencolor("black")


# Given the index of a square in the 2-dimensional array.
# Return the position of the square.
def get_position(indexx,indexy,size=g_size_of_square):
    x = (-2.7+1.1*indexx)*size
    y = (1.7-1.1*indexy)*size
    return (x,y)


# The inverse of get_position.
# Given position, return the indices of the square in the array.
def judge_position_index(x,y):
    index_x = math.floor(\
        (x/g_size_of_square-0.501)/g_relative_size_of_delta)+3
    index_y = 1-math.floor(\
        (y/g_size_of_square-0.501)/g_relative_size_of_delta)
    return (index_x,index_y)


# Event to be bound with onclick.
def clickEvent(x,y):
    global g_current,g_status
    # The situation when the user choose a square in the board.
    if abs(x) <= 2.7*g_size_of_square and abs(y) <= 2.7*g_size_of_square:
        if not g_current == (-1,-1):
            clear_square(g_current[0],g_current[1])
        index_x,index_y = judge_position_index(x,y)
        g_current = (index_x,index_y)
        startx = (-2.7+1.1*index_x)*g_size_of_square
        starty = (1.7-1.1*index_y)*g_size_of_square
        draw_empty_square(startx,starty,g_size_of_square,g_width_of_border)
        g_status = True
    # The situation when user select a color to be flipped to.
    if (g_status == True) \
    and x >= (-2*g_relative_size_of_delta-1)*g_size_of_square\
    and x <= (2*g_relative_size_of_delta)*g_size_of_square\
    and y >= (-1.9-2*g_relative_size_of_delta)*g_size_of_square\
    and y <= (-0.9-2*g_relative_size_of_delta)*g_size_of_square:
        color_index = math.floor(x/(g_relative_size_of_delta*g_size_of_square)+1.001)+2
        if not g_board[g_current[0]][g_current[1]][1].color()[0] == colors[color_index]:
            g_status = False
            clear_square(g_current[0],g_current[1])
            flipcolor(g_current,colors[color_index])
            g_screen.update()
            for i in range(5):
                for j in range(5):
                    g_board[i][j][2] = False


# Draw the color bar.
def draw_bar(size):
    tt.pencolor("silver")
    for i in range(5):
        draw_colored_square(-0.5+i,5.4,size,colors[i])
        relative_position = get_position(-0.5+i,5.4)
        draw_empty_square(relative_position[0],relative_position[1],width=g_width_of_border/2)


# Draw the 5*5 board.
def draw_board(size):
    for i in range(5):
        for j in range(5):
            g_board[i][j][1] = draw_colored_square(\
                i,j,size,colors[g_board[i][j][0]])


# The recursive function to flip the color.
def flipcolor(startpos,col):
    x = startpos[0]
    y = startpos[1]
    current_col = g_board[x][y][1].color()
    g_board[x][y][1].color(col)
    g_board[x][y][2] = True
    if x >= 1 and x <= 3:
        if g_board[x+1][y][1].color() == current_col:
            if g_board[x+1][y][2] == False:
                flipcolor((x+1,y),col)
        if g_board[x-1][y][1].color() == current_col:
            if g_board[x-1][y][2] == False:
                flipcolor((x-1,y),col)
    elif x == 0:
        if g_board[x+1][y][1].color() == current_col:
            if g_board[x+1][y][2] == False:
                flipcolor((x+1,y),col)
    elif x == 4:
        if g_board[x-1][y][1].color() == current_col:
            if g_board[x-1][y][2] == False:
                flipcolor((x-1,y),col)

    if y >= 1 and y <= 3:
        if g_board[x][y+1][1].color() == current_col:
            if g_board[x][y+1][2] == False:
                flipcolor((x,y+1),col)
        if g_board[x][y-1][1].color() == current_col:
            if g_board[x][y-1][2] == False:
                flipcolor((x,y-1),col)
    elif y == 0:
        if g_board[x][y+1][1].color() == current_col:
            if g_board[x][y+1][2] == False:
                flipcolor((x,y+1),col)
    elif y == 4:
        if g_board[x][y-1][1].color() == current_col:
            if g_board[x][y-1][2] == False:
                flipcolor((x,y-1),col)
    return


# Game body
init_board_info()
draw_board(g_size_of_square)
draw_bar(g_size_of_square)
tt.pencolor("black")
screen = tt.getscreen()
screen.onclick(clickEvent)
screen.mainloop()

