"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    w=Tk()
    w.withdraw()
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    prime = simpledialog.askinteger(None, prompt='Can  you give me a number between 1-100?')
    if prime < 2:

        for i in range(2, prime/2):
            if(prime%i==0):
                messagebox.showinfo(None, message='This number is not prime')
                break



pass
