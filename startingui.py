from tkinter import *
from tkinter import ttk


class StartingUi:
    def __init__(self, data):
        self.data = data
        self.window = Tk()
        self.window.title("Welcome to TutorialsPoint")
        self.window.geometry('300x610')
        Label(self.window, text="Department").grid(row=0, column=0)
        Label(self.window, text="Course Number").grid(row=1, column=0)
        self.dept_name = StringVar()
        self.course_num = StringVar()
        Entry(self.window, textvariable=self.dept_name).grid(row=0, column=1)
        Entry(self.window, textvariable=self.course_num).grid(row=1, column=1)
        ttk.Button(self.window, command=self.add_course, text="Add").grid(row=2, column=1)
        self.course_list = Listbox(self.window)
        self.course_list.grid(row=3, column=0, columnspan=2, pady=15)

        Label(self.window, text="Notify email").grid(row=4, column=0)
        self.email = StringVar()
        Entry(self.window, textvariable=self.email).grid(row=4, column=1)
        ttk.Button(self.window, command=self.add_email, text="Add").grid(row=5, column=1)
        self.email_list = Listbox(self.window)
        self.email_list.grid(row=6, column=0, columnspan=2, pady=15)

        Label(self.window, text="Sleep time").grid(row=7, column=0)
        self.max_sleep_time = StringVar()
        Entry(self.window, textvariable=self.max_sleep_time).grid(row=7, column=1)
        ttk.Button(self.window, command=self.finish, text="Finish").grid(row=8, column=1)
        self.window.mainloop()

    def add_course(self):
        dept_name = self.dept_name.get().upper()
        course_num = self.course_num.get()
        if len(dept_name) == 4 or len(course_num) == 3:
            self.course_list.insert(END, dept_name + " " + course_num)
            url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=" \
                  + dept_name + "&course=" + str(course_num)
            self.data.urls.append(url)

            self.dept_name.set("")
            self.course_num.set("")

    def add_email(self):
        email = self.email.get()
        if True:
            self.email_list.insert(END, email)
            self.data.recipients.append(email)
            self.email.set("")

    def finish(self):
        self.data.max_sleep_time = int(self.max_sleep_time.get())
        self.window.destroy()
