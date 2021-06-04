import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(file="bg-cherep.png")
        tk.Label(self, image=self.img).pack(side="top", fill="both", expand="no")
        self.i2 = tk.PhotoImage(file="ok_accept_17936.png")
        tk.Label(self, image=self.i2).place(x=10, y=10)
        #self.geometry(f"300x520+{int(1920/2-300/2)}+200")
        self.title = "Bets Calculator"
        #tk.Button(self, text="OKKK!!!").place(x=10, y=50)
        #tk.Entry(self, text="afnalsknfan", font=("Aial", 17)).place(x=200,y=400, width=20)
    def run(self):
        self.mainloop()

