'''
Sean Collings, Assignment 4 Task 2
I've seperated my program into functions to make it a bit more readable
I wrote a get_user_input function which will prevent non-integer / float data from crashing the program
and require the user to re-enter if they do enter anything that isn't a number.
The values get returned from that function as floats and then the volume and surface area are calculated
'''


def main():
    print("Welcome to the Sean's cuboid calculator extrodinare!")
    print("You will know enter the Length, Height, and Width of your cuboid in feet")

    length, height, width = get_user_input()

    # Rounding the values to 32 decimal points to get rid of floating-point rounding errors
    volume = round(length * width * height, 32)
    surface_area = round((length * height * 2) + (length * width * 2) + (height * width * 2), 32)

    print("Your %s X %s X %s cuboid has a volume of %s cubic feet and a surface area of %s square feet." 
        %(length, height, width, volume, surface_area))

    # Check some other data for neato extra facts!
    if length == width == height:
        print("Your cuboid also happens to be a square")
    # I could add more, but there are that many interesing things about a cuboid

def get_user_input():
    valid_user_input = False # will only be set to true if all 3 values are valid ints / floats 
    while not valid_user_input:
        try:
            length =  float(input("Enter Length >>> "))
            height =  float(input("Enter Height >>> "))
            width  =  float(input("Enter Width  >>> "))
            valid_user_input = True
        except ValueError:
            print("Looks like something you entered wasn't a number, please try again")
    return (length, height, width) 

main()