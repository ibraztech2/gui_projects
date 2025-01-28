def create_task():
    date_checked = ""
    get_completion_date_input = IntVar()
    task_status = False
    date_created = datetime_stamp
    task_list.append(f"{task_entry.get()}~{task_status}~{date_created}~{date_checked}")
    save_task()
    display_task()



def delete_task():
    global delete_task_call
    delete_task_call=True
    delete_response = messagebox.askyesno("Delete","press okay to delete task")
    if delete_response:
        if not task_entry.get():
            if task_listbox.curselection():
                get_current_selection = task_listbox.curselection()
                get_current_selection = len(task_list)- int(get_current_selection[0]) -1
                task_list.pop(get_current_selection)

        else:
            messagebox.showerror("Error", "Task input entry contain unsaved tasks")
        save_task()
        display_task()
        delete_task_call = False


def display_task():
    task_listbox.delete(0, END)

    for task in task_list:
        current_task,status,date_created,date_checked = task.split("~")
        if date_checked :
            if status == "True":
                task_listbox.insert(0,f"Task:{current_task} Status: Completed ")
            else:
                task_listbox.insert(0,f"Task:{current_task} Status: Not Completed")

        else:
            task_listbox.insert(0,f"Task:{current_task} Status: Not Completed")



def check_task():
    global check_task_call
    check_task_call=True
    get_current_selection = task_listbox.curselection()
    if get_current_selection:
        get_current_selection = len(task_list) - int(get_current_selection[0]) - 1
        task = task_list[get_current_selection]
        current_task, status, date_created, date_checked = task.split("~")
        new_status = "True" if status == "False" else "False"
        check_datetime_stamp = datetime_stamp
        task_list[get_current_selection] =f"{current_task}~{new_status}~{date_created}~{check_datetime_stamp}"
        save_task()
        display_task()
    else:
        messagebox.showerror("Check Error","Please select a task to check/Uncheck")

    check_task_call = False

def save_task():
    if task_entry.get() or delete_task_call or check_task_call:
        with open(text_file_path, "w") as files:
            for task in task_list:
                current_task, status, date_created, date_checked = task.split("~")

                if task:
                    files.write(f"{current_task}~{status}~{date_created}~{date_checked}\n")

        display_task()

    else:
        messagebox.showerror("Error", f"Error, input task !!! ")
    task_entry.delete(0, END)


def task_file_to_list():
    if path.exists(text_file_path):
        with open(text_file_path, "r") as tasks:
            for task in tasks:
                task_list.append(task.strip())


def load_task():
    if path.exists(text_file_path):
        task_file_to_list()
        display_task()
def task_details():
    get_current_selection = task_listbox.curselection()
    if get_current_selection:
        get_task_details_val = task_detail_contl_var.get()
        get_current_selection = len(task_list) - int(get_current_selection[0]) - 1
        if get_task_details_val:
            current_task, status, date_created, date_checked = task_list[get_current_selection].split("~")
            print(task_list[get_current_selection])
            messagebox.showinfo(f"{current_task} Details",f"Task: {current_task}\n"
                                                          f"Status: {"completed" if status == "True" else "Not Completed"}\n"
                                                          f"Date Created: {date_created}\n"
                                                          f"Date checked: {date_checked if status == "True" else "Not Checked yet"}")
    else:
        messagebox.showerror("Show Details Error", "Please select task to show its details")



def exit_todo():
    exit_response = None
    if not task_entry.get():
        exit_response = messagebox.askokcancel("Exit", "Press okay to Exit App")
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
datetime_stamp = datetime.fromtimestamp(time_stamp)


task_list = []
delete_task_call = False
check_task_call = False
font, button_width, button_height = ("Arial", 15), 15, 2
text_file_path = "task_data.txt"
list_width = 60
task_detail_contl_var = BooleanVar()

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
task_details_button = Checkbutton(todo_list_frame_1, anchor="center", justify="center",height=button_height, width=button_width,
                                text="Show Task Details", command=task_details,onvalue=True,offvalue=False,variable=task_detail_contl_var,state="active")

#Frame subwidget Grid center
pady, padx = 10, 20
todo_list_title_label.grid(row=0, column=0, columnspan=3)
task_entry.grid(row=1, column=0, padx=padx, pady=pady, ipady=pady + 5, ipadx=padx,columnspan=3)
button_frame.grid(row=2, column=1, columnspan=3, pady=pady, padx=padx)
task_listbox.grid(row=3, column=1, columnspan=3, pady=pady, padx=padx, sticky="nsew")
task_details_button.grid(row=4,column=0,columnspan=3)

create_button.grid(row=0, column=1)
check_task_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
save_button.grid(row=1, column=2)
delete_button.grid(row=2, column=1)


# MainFrame Grid
todo_list_frame_1.grid(row=0, column=0)

#todo_list_main_window.geometry("400x400")
todo_list_main_window.mainloop()
