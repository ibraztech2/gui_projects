import time
from tkinter import *
from datetime import *
from time import time
from os import path
from tkinter import messagebox




class ToDoList:
    def __init__(self, master=Tk(), button_height=2,button_width = 15,entry_width = 60):
        self.master,self.button_height,self.button_width,self.entry_width = master,button_height,button_width,entry_width
        self.taskList = []
        self.filePath = "task_data.txt"
        self.font = ("Arial",15)
        self.getShowProperties = BooleanVar()


        self.activateToDoList()

    def load(self):
        if path.exists(self.filePath):
            with open(self.filePath,"r") as files:
                for task in files:
                    if "~" in task:
                        self.taskList.append(task.strip())
                self.display()


    def display(self):
        self.taskListBox.delete(0, END)

        for task in self.taskList:
            current_task, status, date_created, completion_date = task.split("~")
            if completion_date:
                if status == "True":
                    self.taskListBox.insert(0, f"Task:{current_task} Status: Completed ")
                else:
                    self.taskListBox.insert(0, f"Task:{current_task} Status: Not Completed  To be completed on {completion_date}")

            else:
                self.taskListBox.insert(0, f"Task:{current_task} Status: Not Completed  To be completed on {completion_date}")


    def createTask(self):
        self.getTask = self.taskEntry.get()
        self.status = False

        self.dateCreated = datetime.fromtimestamp(time())
        if self.getTask:
            completion_date= f"{self.getCurrentYear.get()}-{self.getCurrentMonth.get()}-{self.getCurrentDay.get()}"
            self.taskList.append(f"{self.getTask}~{self.status}~{self.dateCreated}~{completion_date}")
        self.saveTask()
        self.display()
        self.taskEntry.delete(0,END)

    def addDate(self):
        self.getCurrentDay = IntVar()
        self.getCurrentMonth = IntVar()
        self.getCurrentYear = IntVar()
        self.currentYear = datetime.fromtimestamp(time()).year
        self.currentMonth =  1 if self.getCurrentYear.get() > self.currentYear  else datetime.fromtimestamp(time()).month
        self.currentDay =  1 if self.getCurrentMonth.get() > self.currentMonth  else datetime.fromtimestamp(time()).day

        if self.taskEntry.get():
            self.topLevel_DateWindow  = Toplevel(self.todo_list_frame_1)
            self.topLevel_DateWindow.title("Date of Completion")
            displayday = Label(self.topLevel_DateWindow,text="Day")
            displaymonth = Label(self.topLevel_DateWindow,text="Month")
            displayyear = Label(self.topLevel_DateWindow,text="Year")
            self.getDay  = Spinbox(self.topLevel_DateWindow, from_=self.currentDay, to=30, increment=1, textvariable=self.getCurrentDay,width=10,font=self.font)
            self.getMonth  = Spinbox(self.topLevel_DateWindow, from_=self.currentMonth, to=12, increment=1, textvariable=self.getCurrentMonth,width=10,font=self.font)
            self.getYear  = Spinbox(self.topLevel_DateWindow, from_=self.currentYear, to=self.currentYear + 50, increment=1, textvariable=self.getCurrentYear,width=10,font=self.font)
            self.doneButton = Button(self.topLevel_DateWindow, command=self.topLevel_DateWindow.destroy, text="Save Date", padx=5, pady=5)

            # topLevel_DateWindow child widget
            displayday.grid(row=0,column=0)
            displaymonth.grid(row=0,column=1)
            displayyear.grid(row=0,column=2)
            self.getDay.grid(row=1,column=0)
            self.getMonth.grid(row=1,column=1)
            self.getYear.grid(row=1,column=2)
            self.doneButton.grid(row=2,column=0,columnspan=3)
        else:
            messagebox.showerror("Error","Input task First !!!")


    def saveTask(self):
        if path.exists(self.filePath):
            if self.taskEntry.get() or self.delete_check:
                with open(self.filePath,"w") as files:
                    for task in self.taskList:
                        if "~" in  task:
                            current_task, status, date_created, completion_date = task.split("~")
                            files.write(f"{current_task}~{status}~{date_created}~{completion_date}\n")

        else:
            messagebox.showerror("Error","Error opening file")



    def deleteTask(self):
        get_current_selection = self.taskListBox.curselection()
        get_current_selection = len(self.taskList) - 1 - get_current_selection[0]
        self.taskList.pop(get_current_selection)
        self.delete_check = True
        self.saveTask()
        self.display()
        self.delete_check = False


    def checkTask(self):
        get_current_selection = self.taskListBox.curselection()
        get_current_selection =len(self.taskList) - 1 - get_current_selection[0]
        task,status,date_created,completion_date  = self.taskList[get_current_selection].split("~")
        status = "False" if status == "True" else "True"
        self.taskList[get_current_selection] = f"{task}~{status}~{date_created}~{completion_date}"
        self.saveTask()
        self.display()

    def showDetails(self):
        get_current_selection = self.taskListBox.curselection()
        if get_current_selection:
            get_current_selection = get_current_selection[0]
            if self.getShowProperties.get():
                task, status, date_created, completion_date = self.taskList[len(self.taskList)-1-get_current_selection].split("~")
                messagebox.showinfo(f"{task} Details,Task: {task}\n "
                                    f"Status: {"completed" if status == "True" else "Not Completed"}\n"
                                    f"Date Created: {date_created}\n"
                                    f"Due Date: {completion_date}")

        else:
            messagebox.showerror("Error","Please Select a Task ")

    def exitToDo(self):
        exit_response = None
        quit_unsaved_exit_response = False
        if not self.taskEntry.get():
            exit_response = messagebox.askokcancel("Exit", "Press okay to Exit App")
        else:
            exit_response = messagebox.askyesnocancel("Unsaved Tasks", "You have unsaved tasks, press Yes continue")
            print(exit_response)
            if exit_response:
                exit_response = messagebox.askyesno("Save before exit", "Press yes to save before Exit")
                if exit_response:
                    self.saveTask()
                    messagebox.askokcancel("Saved", "Saved Successfully")
                else:
                    exit_response = True
            elif not exit_response:
                quit_unsaved_exit_response = True
            elif exit_response is None:
                pass


        if exit_response or quit_unsaved_exit_response:
            self.master.destroy()

    #Gui Management start from here


    def geometryHandler(self):
        self.todo_list_frame_1 = Frame(self.master)

    def initializeWidget(self):
        self.title = Label(self.todo_list_frame_1,text="ToDo List",font=("Arial",30),justify="center")
        self.buttonFrame = Frame(self.todo_list_frame_1)
        self.taskEntry = Entry(self.todo_list_frame_1,width=self.entry_width,font=self.font)
        self.taskListBox = Listbox(self.todo_list_frame_1,width=self.entry_width,font=self.font)
        self.detailsFrame = Frame(self.todo_list_frame_1)

        self.addDateButton = Button(self.buttonFrame, width=self.button_width, height=self.button_height, text="Add Date", justify="center", command=self.addDate)
        self.deleteTaskButton = Button(self.buttonFrame, width=self.button_width, height=self.button_height, text="Delete", justify="center", command=self.deleteTask)
        self.saveTaskButton = Button(self.buttonFrame, width=self.button_width, height=self.button_height, text="Save", justify="center", command=self.createTask)
        self.checkTaskButton = Button(self.buttonFrame, width=self.button_width, height=self.button_height, text="Check/Uncheck", justify="center", command=self.checkTask)
        self.exitToDoButton = Button(self.buttonFrame, width=self.button_width, height=self.button_height, text="Exit", justify="center", command=self.exitToDo)

        self.detailsButton = Checkbutton(self.detailsFrame,text="show Properties",command=self.showDetails,variable=self.getShowProperties,onvalue=True,offvalue=False)






    def grid_handlers(self):
        # Todo child Widget
        self.title.grid(row=0,column=0,pady=20,padx=20)
        self.taskEntry.grid(row=1,column=0,pady=5,padx=20)
        self.buttonFrame.grid(row=2,column=0,pady=20,padx=20)
        self.taskListBox.grid(row=3,column=0,pady=5,padx=5)
        self.detailsFrame.grid(row=4,column=0)

        # Button Frame Child widget
        self.addDateButton.grid(row=0, column=1)
        self.checkTaskButton.grid(row=1, column=0)
        self.exitToDoButton.grid(row=1, column=1)
        self.saveTaskButton.grid(row=1, column=2)
        self.deleteTaskButton.grid(row=2, column=1)

        #details frame child widget
        self.detailsButton.grid(row=0,column=0,columnspan=3)



        self.todo_list_frame_1.grid(row=0, column=0)
        self.master.mainloop()


    #This Method manage all the default method  of the app
    def activateToDoList(self):
        self.geometryHandler()
        self.initializeWidget()
        self.load()
        self.grid_handlers()


