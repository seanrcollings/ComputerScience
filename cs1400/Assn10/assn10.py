'''
Sean Collings
CS1400-2
Assignment 10
'''

#### Add Import Statement(s) as needed ####
from task1 import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####

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