"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

if __name__ == '__main__':
    jack = turtle.Turtle()
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pet = simpledialog.askstring(None, prompt="which pet do you want? dog,eagle,shark, mountain lion, panda or anything")

    happylevel =0

    activities = simpledialog.askstring(None, prompt="What do you want to do with your " + pet + ". Such as feed,walk,do not care and play")
    if activities == 'feed' or activities =='walk' or activities == 'play':
        happylevel+=1
        messagebox.showinfo(None, message="Your pets happylevel is " + str(happylevel))
    elif activities == 'do not care':
        happylevel-=1
        messagebox.showinfo(None, message="Your pets happylevel is " + str(happylevel))
pass
