"""
Have the turtle draw a row of houses.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':

    window=Tk()
    window.withdraw()
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.




    jack = turtle.Turtle()
    jack.penup()
    jack.goto(-300, -300)
    jack.pendown()
    jack.left(90)
    jack.pensize(2)
    def roof(roof):

        if roof == 'pointy':
            jack.right(45)
            jack.forward(35)
            jack.right(90)
            jack.forward(35)
            jack.right(45)
        elif roof == 'flat':
            jack.right(90)
            jack.forward(50)
            jack.right(90)

    def house(size, roof1):
        length = 0
        if size == 'small':
            length = 60
        elif size == "medium":
            length = 120
        elif size =="large":
            length = 250

        jack.forward(length)
        roof(roof1)
        jack.forward(length)

    def grass():
        jack.left(90)
        jack.pencolor('green')
        jack.pensize(5)
        jack.forward(50)
        jack.left(90)
        jack.pencolor('black')
        jack.pensize(2)
    for i in range(8):
        user_size = simpledialog.askstring(None, prompt='what size do you want your house to be?(small, medium, large)')
        user_roof = simpledialog.askstring(None, prompt='Do you want a pointy roof or a flat roof?')
        house(user_size, user_roof)
        grass()











    window.mainloop()
