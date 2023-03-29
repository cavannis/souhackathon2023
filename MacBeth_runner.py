from Classgui import GUI
from Thief import thief
from Dishwasher import dishwasher
from Dogwalker import dogwalker
from Muffinman import muffinman
from Crazedhomelessman import crazedhomelessman
from Swordsman import swordsman
from Textinputgui import TextInputGUI
from Slowprint import Slowprinter

from collections import deque
def main():
    # create a stack to keep track of the user's previous choices
    choice_stack = deque()

    slow_printer = Slowprinter(delay=0.00) # creates a slowest text speed


    slow_printer.slow_print("Welcome to your exotic Macbeth experience. You will choose how Macbeth starts along his journey and will be able to make unique choices along the journey") 

    slow_printer.slow_print("choose what career, job, and name Macbeth has started with in his Journey to become king of scotland. This will affect how easy or hard certain events are")

    slow_printer.slow_print("Macbeths possible career options are as follows: Dishwasher, thief, Swordsman, Dog walker, Muffin man, and crazed homeless man")

    gui = GUI([ "Thief" , "Muffin Man" , "Swordsman", "Dog walker", "Crazed Homeless Man", "Dishwasher"]) # creates the gui where you select your class.

    gui.mainloop() # run the GUI main loop

    Classchoice = gui.get_selected_option() # saves the selection from the class gui

    slow_printer.slow_print("you have selected: " + Classchoice )

    slow_printer.slow_print("now that you selected your class, it's time to select your weapon!")

    if Classchoice == "Thief":
        Weapon = thief()
    elif Classchoice == "Muffin Man":
        Weapon = muffinman()
    elif Classchoice == "Swordsman":
        Weapon = swordsman()
    elif Classchoice == "Dishwasher":
        Weapon = dishwasher()
    elif Classchoice == "Crazed Homeless Man":
        Weapon = crazedhomelessman()
    elif Classchoice == "Dog walker":
        Weapon = dogwalker()

    weapons = Weapon.getweapons() 
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]

    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]

    gui = GUI(options, previous_gui=gui) # Add the previous_gui argument to create the back button
    gui.mainloop()

    Weapon_choice = gui.get_selected_option()
    choice_stack.appendleft(("weapon", Weapon_choice))
    print("You selected:" + Weapon_choice)
    
    slow_printer.slow_print("now to select your name!")
    text_input_gui = TextInputGUI("now to select your name!")
    name = text_input_gui.get_input()

    slow_printer.slow_print("wecome: " + name + " you are a: " + Classchoice + " with a weapon choice of " + Weapon_choice)
    choice_stack.appendleft(("name", name))

    slow_printer.slow_print(name + " You are locked in a cell and need to get out. There is a lock on the door that you can reach. What do you do?")
    gui = GUI(["Kick the door down", "look for something to pick the lock", "scream for no reason", "try pulling on the lock"])
    gui.mainloop()

    DoorChoice = gui.get_selected_option()
    
    
if __name__ == "__main__":
    main()

