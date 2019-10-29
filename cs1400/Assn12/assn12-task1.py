import turtle
tr = turtle.Turtle()

class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def draw_face(self):
        tr.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()

    def __draw_head(self):
        tr.home()
        tr.penup()
        tr.goto(0, -100)
        tr.pendown()
        tr.color('black', 'yellow' if self.__happy else 'red')
        tr.begin_fill()
        tr.circle(100)
        tr.end_fill()

    def __draw_eyes(self):
        tr.color('black', 'black' if self.__dark_eyes else 'blue')
        
        tr.penup()
        tr.goto(30, 20)
        tr.pendown()
        tr.begin_fill()
        tr.circle(15)

        tr.penup()
        tr.goto(-30, 20)
        tr.pendown()
        tr.circle(15)

        tr.end_fill() 

    def __draw_mouth(self):
        tr.pensize(8)   
        if self.__smile:
            tr.penup() 
            tr.goto(-60, -40)
            tr.pendown()
            tr.setheading(317)            
        else:
            tr.penup() 
            tr.goto(60, -45)
            tr.pendown()
            tr.setheading(135)

        tr.circle(90, 90) 
        tr.pensize(1)



def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()