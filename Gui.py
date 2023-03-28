import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Options")
        self.geometry("300x200")
        
        # create a label
        label = tk.Label(self, text="Select an option:")
        label.pack(pady=10)

        # create a list of options
        options = ["DishWasher", "Thief", "Dog Walker", "Crazed Homless Man", "Swordsman", "Muffin Man"]

        # create a radio button for each option
        self.selected_option = tk.StringVar()
        for option in options:
            rb = tk.Radiobutton(self, text=option, variable=self.selected_option, value=option)
            rb.pack()

        # create a button to submit the selection
        submit_button = tk.Button(self, text="Submit", command=self.submit_selection)
        submit_button.pack(pady=10)

    def submit_selection(self):
        selected = self.selected_option.get()
        print(f"Selected option: {selected}")

# create and run the GUI
gui = GUI()
gui.mainloop()
