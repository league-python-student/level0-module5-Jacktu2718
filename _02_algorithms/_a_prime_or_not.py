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
    prime = simpledialog.askinteger(None, prompt='Can  you give me number that you want to know if it is prime?')
    number = prime

    if number > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (number // 2) + 1):

            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


pass