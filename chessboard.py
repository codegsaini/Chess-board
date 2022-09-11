"""
Project Title : ChessBoard using Turtle
Author        : Gaurav Saini
Description   : The project is made during the internship period at Techinest
Letter Id     : TECHS26103177

"""

import turtle as pen

def drawBox(board, x, y, size, fillColor) :
    board.penup()                # disallow pen to draw
    board.goto(x, y)             # move pen to the specified coordinates
    board.pendown()              # allow the pen to draw

    board.fillcolor(fillColor)   # setting the color to be filled

    board.begin_fill()           # start drawing the box

    for i in range(0, 4):        # this loop will make a box      
        board.forward(size)
        board.right(90)

    board.end_fill()             # stop drawing

# This function will draw the chess board
def drawChessBoard() :
    square_color = "black" # Taking the color of first box as black
    start_x = 0            # starting with 0  on x axis
    start_y = 0            # starting with 0 on y -axis
    boxSize = 30           # declaring size of one box

    for i in range(0, 8):  # this loop will help in drawing 8 rows
        for j in range(0, 8): # this loop will help in drawing 8 boxes in a single row
            drawBox(board, start_x+j*boxSize, start_y+i*boxSize, boxSize, square_color)  # draw single box
            square_color = "black" if square_color == "white" else "white" # change the color
        square_color = "black" if square_color == "white" else "white" # change the color for the first box of next row


# initialize board variable as a turtle object
board = pen.Turtle()

# setting the speed of drawing
board.speed(10)

# calling `drawChessBoard()` function to start the drawing
drawChessBoard()

# stop the drawing
pen.done()