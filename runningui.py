from tkinter import *
from tkinter import ttk


class RunningUi:
    def __init__(self):
        self.tasks = []
        self.window = Tk()
        self.window.title("Running")
        self.window.geometry('200x610')
        Label(self.window, text="Running").grid(row=0, column=0)
        self.running_list = Listbox(self.window)
        self.running_list.grid(row=1, column=0, columnspan=1, pady=15)
        ttk.Button(self.window, command=self.stop, text="Stop").grid(row=2, column=0)

    def start(self, tasks):
        self.tasks = tasks
        self.window.mainloop()

    def stop(self):
        for task in self.tasks:
            task.finished = True
        self.window.destroy()

    def show_msg(self, msg):
        self.running_list.insert(END, msg)
