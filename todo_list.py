"""             To Do list
This Enable the user to create a list of task which can managed efficiently with respect to their time and date of execution
This will have :
    1. Take user list of task
    2. Task description
    3. Date of task created
    4. checkbutton to track the status of completed task
    4. can even user task completion habit
    5. classify task as Work, self-help, financial intelligence

    """

from tkinter import *
import datetime, time
from os import makedirs

todo_list_main_frame = Tk()
todo_list_main_frame.geometry("400x400")
new_task_frame = LabelFrame(todo_list_main_frame)
button_width = 13
button_height = 2


def text_input():
    get_check_button_value = IntVar()
    new_task_entry = Entry(new_task_frame, width=30, justify="center", state="normal")
    new_task_Check_button = Checkbutton(new_task_frame, offvalue=1, onvalue=0,
                                        command=lambda value=get_check_button_value: check_mark_task(value))
    done_button = Button(new_task_frame, text="Done")

    title_label = Label(todo_list_main_frame, text="ToDo List ", font=("Arial", 20), justify="center", fg="blue")
    Button(todo_list_main_frame, text="Create New Task", command=create_new_task, justify="center",
           height=button_height, width=button_width).grid(row=2, column=0)
    Button(todo_list_main_frame, text="Delete Task", command=delete_task, justify="center", height=button_height,
           width=button_width).grid(row=2, column=1)
    Button(todo_list_main_frame, text="Exit", command=todo_list_main_frame.destroy, justify="center",
           height=button_height, width=button_width).grid(row=2, column=2)
    #Button(todo_list_main_frame,text="Create New Task",command=create_new_task)

    new_task_Check_button.grid(row=0, column=0)
    new_task_entry.grid(row=0, column=1)
    done_button.grid(row=0, column=2)

    new_task_frame.grid(row=1, column=0, columnspan=3)
    title_label.grid(row=0, column=1)


def create_new_task():
    pass


def delete_task():
    pass


def check_mark_task(value):
    pass


def save_file():
    time_stamp = time.time()
    date_time_stamp = datetime.datetime.fromtimestamp(time_stamp)
    pass
    #make_file_path = makedirs("")


text_input()
todo_list_main_frame.mainloop()

"""    
    todo_displaY_data = Label(todo_list_main_frame)
    meta_data_file  = open(f"{meta_data}.text","w")
    data_entry_file  = open(f"{meta_data[6]}{meta_data[6]}")
    

"""
