import tkinter as tk

class GUI(tk.Tk):
    def __init__(self, options):
        super().__init__()
        self.title("Options")
        self.geometry("300x200")
        
        # create a label
        label = tk.Label(self, text="Select an option:")
        label.pack(pady=10)

        # create a listbox with all the options
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=len(options))
        for option in options:
            self.listbox.insert(tk.END, option)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # create a button to submit the selection
        submit_button = tk.Button(self, text="Submit", command=self.submit_selection)
        submit_button.pack(pady=10)

    def submit_selection(self):
        self.selected = self.listbox.get(self.listbox.curselection())
        self.destroy()

    def get_selected_option(self):
        return self.selected

