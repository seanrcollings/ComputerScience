'''
Sean Collings
CS1400-2
Assignment 10
'''

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    width = input("Please enter the width of the board (default = 250): ")
    height = input("Please enter the height of the board (default = 250): ")
    startX = input("Please enter the starting x coordinate: ")
    startY = input("Please enter the starting y coordinate: ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()