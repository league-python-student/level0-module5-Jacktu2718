import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window=Tk()
    window.withdraw()


    jack = turtle.Turtle()
    for i in range(10):
        jack.speed(20)



        for i in range(4):
            jack.penup()
            jack.forward(200)
            jack.left(90)

        jack.right(45)
        jack.forward(200)
        for i in range(2):
            jack.left(45)
            jack.forward(200)
        jack.left(90)
        jack.forward(282.5)
        jack.left(45)
        jack.forward(290)
        jack.pendown()
        for i in range(20):
            jack.speed(15)
            jack.circle(200)
            jack.forward(10)
        jack.penup()
        for i in range(10):
            jack.forward(10)
            for i in range(3):
                jack.forward(200)
                jack.left(90)
        jack.forward(100)
        jack.pendown()
        for i in range(20):
            jack.circle(200)
            jack.forward(10)
        jack.forward(150)
        for i in range(20):
            jack.circle(200)
            jack.forward(10)





    window.mainloop()
