def create_task():
    task_status = False
    task_list.append(f"{task_entry.get()},{task_status},{task_datetime_stamp}")
    save_task()
    display_task()


def delete_task():
    global delete_task_call
    delete_task_call=True
    #task_listbox.delete(0, END)
    delete_response = messagebox.askyesno("Delete","press okay to delete task")
    if delete_response:
        if not task_entry.get():
            get_current_selection = task_listbox.curselection()
            get_current_selection = int(get_current_selection[0]) +1
            get_current_selection *= -1
            if get_current_selection:
                print(get_current_selection)
                print(task_list)
                task_list.remove(task_list[get_current_selection])

        else:
            messagebox.showerror("Error", "Task input entry contain unsaved tasks")
        save_task()
        display_task()
        delete_task_call = False


def display_task():
    task_listbox.delete(0, END)

    for task in task_list:
        task_stop_index = None
        status_stop_index = None
        time_stamp_stop_index = None
        task_check = False
        for index, letter in enumerate(task):
            if letter == "," and not task_check:
                task_stop_index = index
                task_check = True
            elif letter == "," and task_check:
                status_stop_index = index
                task_check = False
        current_status = task[task_stop_index+1:status_stop_index]
        task_listbox.insert(0,f"Task:{task[0:task_stop_index]} Status: {"completed" if current_status == "True" else "Not Completed"} Date created : {task[status_stop_index+1:time_stamp_stop_index]}")


def check_task():
    get_current_selection = task_listbox.curselection()
    get_current_selection = get_current_selection[0] +1
    get_current_selection *= -1
    task_stop_index = None
    status_stop_index =  None
    task_check = False
    task = task_list[get_current_selection]
    print(task)
    for index, letter in enumerate(task):
        if letter == "," and not task_check:
            task_stop_index = index
            task_check = True
        elif letter == "," and task_check:
            status_stop_index = index
            task_check = False
    current_task_datetime_stamp = task[status_stop_index + 1:]
    if task[task_stop_index+1:status_stop_index] == "False":
        task = f"{task[:task_stop_index]},True,{current_task_datetime_stamp}"
    else:
        task = f"{task[:task_stop_index]},False,{task[status_stop_index:]}"
    task_list[get_current_selection] = task
    print(task)
    display_task()





def save_task():
    if task_entry.get() or delete_task_call:
        with open(text_file_path, "w") as files:
            for task in task_list:
                task_stop_index = None
                status_stop_index = None
                task_check = False
                for index, letter in enumerate(task):
                    if letter == "," and not task_check:
                        task_stop_index = index
                        task_check = True
                    elif letter == "," and task_check:
                        status_stop_index = index
                        task_check = False
                current_task = task[0:task_stop_index]
                task_status = task[task_stop_index+1:status_stop_index]
                current_task_datetime_stamp = task[status_stop_index + 1:]
                if current_task:
                    files.write(f"{current_task},{task_status},{current_task_datetime_stamp } \n")

    else:
        messagebox.showerror("Error", f"Error, input task !!! ")
    task_entry.delete(0, END)


def task_file_to_list():
    if path.exists("task_data.txt"):
        with open("task_data.txt", "r") as tasks:
            for task in tasks:
                task_list.append(task.strip())


def load_task():
    if path.exists("task_data.txt"):
        task_file_to_list()
        display_task()


def exit_todo():
    exit_response = None
    if not task_entry.get():
        exit_response = messagebox.askokcancel("Exit", "Press okay to Exit App")
        exit_response = True
    else:
        exit_response = messagebox.askyesno("Unsaved Tasks", "You have unsaved tasks, press Yes continue")
        print(exit_response)
        if exit_response:
            exit_response = messagebox.askyesno("Save before exit", "Press yes to save before Exit")
            if exit_response:
                save_task()
                messagebox.askokcancel("Saved", "Saved Successfully")
            else:
                exit_response = True

    if exit_response:
        todo_list_main_window.destroy()


from tkinter import messagebox
from tkinter import *
from time import time
from datetime import datetime
from os import path

from tkinter import *

todo_list_main_window = Tk()

time_stamp = time()
task_datetime_stamp = datetime.fromtimestamp(time_stamp)

task_list = []
delete_task_call = False
font, button_width, button_height = ("Arial", 15), 15, 2
get_checkButton_value = BooleanVar()
get_button_text = StringVar()
text_file_path = "task_data.txt"
list_width = 60

todo_list_frame_1 = Frame(todo_list_main_window)
button_frame = Frame(todo_list_frame_1)
todo_list_title_label = Label(todo_list_frame_1, text="ToDo list", justify="center", font=font)
task_entry = Entry(todo_list_frame_1, font=font, justify="left", width=list_width)
task_listbox = Listbox(todo_list_frame_1, font=font, width=list_width)

# Load Previous Tasks
load_task()

check_task_button = Button(button_frame, anchor="center", justify="center",height=button_height, width=button_width,
                                text="check/uncheck task", command=check_task)
create_button = Button(button_frame, text="Create", height=button_height, width=button_width, command=create_task,
                       justify="center")
delete_button = Button(button_frame, text="remove task", height=button_height, width=button_width, command=delete_task,
                       justify="center")
save_button = Button(button_frame, text="Save task", height=button_height, width=button_width, command=save_task,
                     justify="center")
exit_button = Button(button_frame, text="Exit", height=button_height, width=button_width, command=exit_todo,
                     justify="center")

#Frame subwidget Grid center
pady, padx = 10, 20
todo_list_title_label.grid(row=0, column=0, columnspan=3)
task_entry.grid(row=1, column=0, padx=padx, pady=pady, ipady=pady + 5, ipadx=padx)
button_frame.grid(row=2, column=0, columnspan=3, pady=pady, padx=padx)
task_listbox.grid(row=3, column=0, columnspan=3, pady=pady, padx=padx, sticky="nsew")

create_button.grid(row=0, column=1)
check_task_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
save_button.grid(row=1, column=2)
delete_button.grid(row=2, column=1)

# MainFrame Grid handler
todo_list_frame_1.grid(row=0, column=0)

#todo_list_main_window.geometry("400x400")
todo_list_main_window.mainloop()
