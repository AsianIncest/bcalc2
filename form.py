import tkinter as tk


class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "Bets Calculator"
        self.frame = tk.Frame(self.root)
        x = tk.Label(self.frame, text="gsadgasdg")
        x.pack()
        self.frame.pack()

    def run(self):
        self.root.mainloop()

