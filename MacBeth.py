from Classgui import GUI

print("Welcome to your exotic Macbeth experience. You will choose how Macbeth starts along his journey and will be able to make unique choices along the journey") 

print("choose what career/job Macbeth has started with in his Journey to become king of scotland. This will affect how easy or hard certain events are")

print("Macbeths possible career options are as follows: Dishwasher, thief, Swordsman, Dog walker, Muffin man, and crazed homeless man")

gui = GUI(["Dishwasher", "Thief" , "Muffin man" , "Swordsman", "Dog walker", "Crazed Homless Man", "Dishwasher"]) # creates the gui where you select your class.

gui.mainloop() # run the GUI main loop

Classchoice = gui.get_selected_option() # saves the selection from the class gui

print("you have selected: " , Classchoice )

print("now that you selected your class, it's time to select your weapon!")
