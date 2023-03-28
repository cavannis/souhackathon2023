from Classgui import GUI
from Thief import thief
from Dishwasher import dishwasher
from Dogwalker import dogwalker
from Muffinman import muffinman
from Crazedhomelessman import crazedhomelessman
from Swordsman import swordsman
from Textinputgui import TextInputGUI
print("Welcome to your exotic Macbeth experience. You will choose how Macbeth starts along his journey and will be able to make unique choices along the journey") 

print("choose what career/job Macbeth has started with in his Journey to become king of scotland. This will affect how easy or hard certain events are")

print("Macbeths possible career options are as follows: Dishwasher, thief, Swordsman, Dog walker, Muffin man, and crazed homeless man")

gui = GUI([ "Thief" , "Muffin Man" , "Swordsman", "Dog walker", "Crazed Homeless Man", "Dishwasher"]) # creates the gui where you select your class.

gui.mainloop() # run the GUI main loop

Classchoice = gui.get_selected_option() # saves the selection from the class gui

print("you have selected: " , Classchoice )

print("now that you selected your class, it's time to select your weapon!")

if Classchoice == "Thief":
    
    T = thief()
    
    weapons = T.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)

if Classchoice == "Muffin Man":
    mm = muffinman()
    
    weapons = T.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)

if Classchoice == "Swordsman":
    sw = swordsman()
    
    weapons = sw.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)
    
if Classchoice == "Dishwasher":
    dish = dishwasher()
    
    weapons = dish.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)
    
if Classchoice == "Crazed Homeless Man":
    chm = crazedhomelessman()
    
    weapons = chm.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)
    
if Classchoice == "Dog Walker":
    dw = dogwalker()
    
    weapons = dw.getweapons()
    
    weapons_list = [weapon.strip() for weapon in weapons.split(",")]
    
    options = [f'{weapon_word.strip()}' for weapon in weapons_list for weapon_word in weapon.split()]
    
    gui = GUI(options)
    gui.mainloop()
    Weapon_choice = gui.get_selected_option()
    
    print("You selected :", Weapon_choice)
    

text_input_gui = TextInputGUI("now to select your name!")
name = text_input_gui.get_input()
print("wecome:", name, " you are a:", Classchoice , "with the weapon:", Weapon_choice)

