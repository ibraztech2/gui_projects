from tkinter import *

operand = ""
operand_1 = None
operand_2 = None
operator_sign = None
operand_expression = ""
result_eval = None


def button_click(value):
    global operand, operator_sign, operand_2, operand_1, operand_expression
    if value not in "+-/*=C":
        entry.delete(0, END)
        operand = operand + str(value)
        entry.insert(0, operand)

    if value in "*+/-":
        operand_1 = entry.get()
        operator_sign = value
        entry.delete(0, END)
        entry.insert(0, value)
        operand = ""

    elif value == "=":
        operand_2 = entry.get()
        operand_expression = f"{operand_1}{operator_sign}{operand_2}"
        if not (operand_2 is None and operand_1 is None and operator_sign is None):
            solve(operand_expression)
        reset_operands()
    elif value == "C":
        entry.delete(0, END)
        reset_operands()


def reset_operands():
    global operand_1, operand_2, operand, result_eval
    operand_1 = ""
    operand_2 = ""
    operand = ""
    result_eval = 0


def solve(operand_expression):
    global result_eval
    try:
        result_eval = eval(operand_expression)
        entry.delete(0, END)
        entry.insert(0, result_eval)
        disp_previous_result_check()
    except ZeroDivisionError as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
        reset_operands()
        print(f"This Error is due to {e}")
    finally:
        reset_operands()


def disp_previous_result(state_value):
    if state_value:
        entry.delete(0, END)
        entry.insert(0, operand_expression)
    elif not state_value:
        entry.delete(0, END)
        entry.insert(0, result_eval)


def disp_previous_result_check():
    previous_control_variable = IntVar()
    if result_eval is None:
        Checkbutton(meta_label_frame, text="Disp previous", background="white", fg="blue", anchor="center",
                    state="disabled").grid(column=2, row=0)
    else:
        Checkbutton(meta_label_frame, text="Disp previous", background="blue", fg="white", anchor="center",
                    state="active", activebackground="blue",
                    command=lambda value=previous_control_variable: disp_previous_result(value), onvalue=True,
                    offvalue=False, variable=previous_control_variable).grid(column=2, row=0)


def meta_label():
    f = " " * 12
    disp_previous_result_check()
    Label(meta_label_frame, text="Ibraztech", fg="BLUE", anchor="e").grid(column=0, row=0)
    Label(meta_label_frame, text=f"{f}", fg="BLUE", background="skyblue", anchor="e").grid(column=1, row=0)
    #Label(meta_label_frame, text=f"{f}", fg="BLUE", background="skyblue",anchor="e").grid(column=2, row=0)
    Label(meta_label_frame, text=f"{f}", fg="BLUE", background="skyblue", anchor="e").grid(column=3, row=0)
    Label(meta_label_frame, text="Meta", fg="BLUE", anchor="center", justify="left").grid(column=4, row=0)


def clr_func():
    reset_operands()
    entry.delete(0, END)


def settings():
    pass


root = Tk()
root.title("Simple Calculator")
pad_x = 150
pad_y = 100
main_calculator_widget = LabelFrame(root, background="skyblue")
main_calculator_widget.grid(row=0, column=0)
meta_label_frame = Label(main_calculator_widget, background="skyblue")
meta_label_frame.grid(row=1, column=0)
meta_label()

entry = Entry(main_calculator_widget, borderwidth=5, border=2, width=39)
entry.grid(row=0, column=0, columnspan=3, pady=10, padx=20)
#Building a simple calculator
buttons = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9",
           "+", "0", "-",
           "/", "C", "*",
           "="]
button_frame = Label(main_calculator_widget, background="skyblue")
button_frame.grid(row=2, column=0)
row_value = 1
column_value = 1
for button in buttons:
    if button == "=":
        row_value += 1
        column_value = 0
        Button(button_frame, text=button, font=("Arial", 12), command=lambda value=button: button_click(value),
               height=3,
               width=19, bg="navyblue", fg="white", activebackground="lightblue", activeforeground="black",
               justify="center").grid(
            row=row_value, column=column_value, columnspan=3)
    else:
        if column_value & 3 == 0:
            row_value += 1
            column_value = 1

        Button(button_frame, text=button, font=("Arial", 12), command=lambda value=button: button_click(value),
               height=3,
               width=9, bg="navyblue", fg="white", activebackground="lightblue", activeforeground="black").grid(
            row=row_value, column=column_value)
        column_value += 1

Button(button_frame, command=settings, text="Settings", background="navyblue", height=2,
       foreground="white", anchor="center", font=("Arial", 16)).grid(row=6, column=3)
Button(main_calculator_widget, text="Exit", command=root.destroy, fg="BLUE", background="lightblue", justify="left",
       width=7, relief="groove", anchor="center", font="Arial,10").grid()
"""
Label(meta_label_frame, text="Ibraztech", fg="BLUE", anchor="e").grid(column=0, row=0)
Label(meta_label_frame, text=" " * 50, background="skyblue", fg="skyblue", anchor="e").grid(column=1, row=0)
Label(meta_label_frame, text="Meta", fg="BLUE", anchor="center", justify="left").grid(column=2, row=0)"""

root.mainloop()
