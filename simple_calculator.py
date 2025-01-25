from pickle import FRAME
from tkinter import Tk, messagebox, Label,Frame, Entry, IntVar, Checkbutton, Button, END


class Calculator:
    def __init__(self):
        self.__root__ = Tk()
        self.operand_1 = None
        self.operand_2 = None
        self.__operand__ = ""
        self.__result__ = None
        self.operandExpression = None
        self.buttons = ["1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9",
                        "+", "0", "-",
                        "/", "C", "*",
                        "=", "Settings", "Exit"]
        self.__rowValue__ = 1
        self.__columnValue__ = 1

    def __displayButton__(self):
        self.metaLabel()

        for button in self.buttons:
            if button == "=":
                Button(self.__buttonFrame__, text=button, font=("Arial", 12), height=self.height,
                       width=self.width * 2 + 1, justify="center", background=self.button_bg,
                       fg="white", activeforeground=self.button_afg,
                       command=lambda __value__=button: self.__buttonClick__(__value__)).grid(row=self.__rowValue__ + 1,
                                                                                              column=1, columnspan=2)
            elif button == "Exit":
                Button(self.__exitFrame__, text="Exit", command=self.exitCallback, fg=self.exitButton_fg,
                       background=self.exitButton_bg, justify="left", activeforeground=self.exitButton_fg,
                       width=self.width, relief="groove", anchor="center", font=("Arial", 10)).grid(
                    row=self.__rowValue__, column=1, columnspan=2)
            elif button == "Settings":
                Button(self.__buttonFrame__, text=button, font=("Arial", 12), height=self.height, width=self.width,
                       justify="center", background=self.button_bg,
                       fg=self.button_fg, activeforeground=self.button_afg,
                       command=self.settingsCallback).grid(row=self.__rowValue__ + 1, column=3)

            else:
                if self.__columnValue__ & 3 == 0:
                    self.__rowValue__ += 1
                    self.__columnValue__ = 1
                Button(self.__buttonFrame__, font=("Arial", 12), text=button, height=3, width=self.width,
                       justify="center", background=self.button_bg, fg=self.button_fg, activeforeground=self.button_afg,
                       command=lambda __value__=button: self.__buttonClick__(__value__)).grid(row=self.__rowValue__,
                                                                                              column=self.__columnValue__)
                self.__columnValue__ += 1

    def __buttonClick__(self, value):

        self.__clickValue__ = str(value)
        if self.__clickValue__ not in "+-*/C=" and (
                self.__clickValue__ != "Exit" and self.__clickValue__ != "Settings"):
            self.__operand__ = self.__operand__ + (self.__clickValue__)
            self.entry.delete(0, END)
            self.entry.insert(0, self.__operand__)
        elif self.__clickValue__ in "*/+-":
            self.__operand__ = ""
            self.__operator__ = self.__clickValue__
            self.operand_1 = self.entry.get()
            self.entry.delete(0, END)
            self.entry.insert(0, self.__operator__)
        elif self.__clickValue__ == "C":
            self.resetOperands()
            self.result = None
        elif self.__clickValue__ == "=":
            self.solve()
            self.resetOperands()

    def buttonParameters(self, frame_bg="skyblue", button_bg="blue", button_fg="white", exitButton_fg="blue",
                         exitButton_bg="lightblue", button_afg="white", height=3, width=9):
        self.button_bg = button_bg
        self.button_fg = button_fg
        self.button_afg = button_afg
        self.height = height
        self.width = width
        self.frame_bg = frame_bg
        self.exitButton_fg = exitButton_fg
        self.exitButton_bg = exitButton_bg

    def displayPreviousResult(self, __value__):
        self.__value__ = __value__
        if self.__value__:
            self.entry.delete(0, END)
            self.entry.insert(0, f"{self.operandExpression}")
        else:
            self.entry.delete(0, END)

    def solve(self):
        self.__operand__ = ""
        self.operand_2 = self.entry.get()
        self.entry.delete(0, END)
        self.operandExpression = f"{self.operand_1}{self.__operator__}{self.operand_2}"
        self.__result__ = eval(self.operandExpression)
        self.entry.insert(0, self.__result__)

    def resetOperands(self):
        self.operand_1 = None
        self.operand_2 = None
        self.__operand__ = ""
        self.operandExpression = None

    def exitCallback(self):
        self.exit_messagebox = messagebox.askyesnocancel("Exit", "Do you want to exit ?")
        if self.exit_messagebox:
            self.__root__.destroy()

    def metaLabel(self):
        self.centerMetaFrame = Label(self.__metaFrameHandler__, width=22, background="skyblue", height=2)
        self.getState = IntVar()

        if self.__result__ == None:
            self.__previousReult_CheckButton__ = Checkbutton(self.__metaFrameHandler__, justify="center", command=lambda
                value=self.getState: self.displayPreviousResult(value),
                                                             onvalue=True, offvalue=False, text="Previous Solution",
                                                             state="disabled")  #activebackground=,activeforeground=,background=)
        else:
            Checkbutton(self.__metaFrameHandler__, justify="center",
                        command=lambda value=self.getState: self.displayPreviousResult(value),
                        onvalue=True, offvalue=False, text="Previous Solution",
                        state="active")  #activebackground=,activeforeground=,background=)
        Label(self.__metaFrameHandler__, text="Ibraztech", fg="blue", background="white").grid(row=0, column=0)

        Label(self.__metaFrameHandler__, text="Meta", fg="blue", background="white").grid(row=0, column=2)
        self.centerMetaFrame.grid(row=0, column=1)

    def settingsCallback(self):
        pass

    def __frameHandler__(self):
        self.__mainCalculatorWidget__ = Label(self.__root__, background=self.frame_bg)
        self.__entryFrameBlank__ = Frame(self.__mainCalculatorWidget__, height=10, width=20,background=self.frame_bg,)
        self.entry = Entry(self.__mainCalculatorWidget__, justify="left", width=40,relief="groove",font=("Arial",8),)
        self.__buttonFrame__ = Label(self.__mainCalculatorWidget__, bg="sky blue")
        self.__metaFrameHandler__ = Label(self.__mainCalculatorWidget__, background="skyblue")
        self.__exitFrame__ = Label(self.__mainCalculatorWidget__, background="lightblue")

    def __gridHandlerAndMainloop__(self):
        self.__mainCalculatorWidget__.grid(row=0, column=0)

        #main Calculator widget child Class
        self.__entryFrameBlank__.grid(row=0,column=0)
        self.entry.grid(row=1, column=0)
        self.__metaFrameHandler__.grid(row=2, column=0)
        self.__buttonFrame__.grid(row=3, column=0)
        self.__exitFrame__.grid(row=4, column=0)
        #entry Frame

        self.__root__.mainloop()

    def calculatorGeometry(self, title, height, width):
        self.__root__.geometry(f"{width}x{height}")
        self.__root__.title(title)

    def activate(self):
        self.buttonParameters()
        self.__frameHandler__()
        self.__displayButton__()
        self.__gridHandlerAndMainloop__()


if __name__ == "main":
    print("Sorry can run stand alone file")
else:
    calculator = Calculator()
