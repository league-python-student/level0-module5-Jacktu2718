"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    jack = turtle.Turtle()
    jack.speed(1)

    def function_1():
        for i in range(4):
            jack.forward(300)
            jack.right(90)


    def function_2():
        for i in range(3):
            jack.forward(400)
            jack.right(120)

    def function_3():
        turtle.circle(500)


    def function_4():
        for i in range(4):
            jack.forward(300)
            jack.right(90)
        for i in range(3):
            jack.forward(300)
            jack.right(120)
        turtle.circle(150)
        jack.forward(300)
        turtle.circle(150)

    shape = simpledialog.askstring(title='shape selector',
                                   prompt='What shape do you want to draw? circle, square,both or triangle')
    if shape == 'circle':
        function_3()
    if shape == 'square':
        function_1()
    if shape == 'triangle':
        function_2()
    if shape == 'both':
        function_4()
    pass
