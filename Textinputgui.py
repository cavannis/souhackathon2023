from tkinter import *

class TextInputGUI:

    def __init__(self, prompt):
        self.root = Tk()
        self.root.title("Text Input")
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.prompt_label = Label(self.frame, text=prompt)
        self.prompt_label.pack(padx=10, pady=10)

        self.input_field = Entry(self.frame, width=30)
        self.input_field.pack(padx=10, pady=10)

        self.ok_button = Button(self.frame, text="OK", command=self.ok_button_clicked)
        self.ok_button.pack(padx=10, pady=10)

        self.value = None

        self.root.mainloop()

    def ok_button_clicked(self):
        self.value = self.input_field.get()
        self.root.destroy()

    def get_input(self):
        return self.value
