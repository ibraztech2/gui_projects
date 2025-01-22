

class Calculator:
    def __init__(self):
        self.operand_1 = None
        self.operand_2 = None
        self.__operand__ = ""
        self.__result__ = None
        self.operandExpression = None
        self.operator = None
        self.buttons = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9",
                   "+", "0", "-",
                   "/", "C", "*",
                   "=","Settings","Exit"]
        self.__rowValue__ = 1
        self.__columnValue__ = 1
        self.__root__ = Tk()




    def __displayButton__(self):
        self.metaLabel()
        width = 9
        height = 3
        for button in self.buttons:
            if button == "=":
                Button(self.__buttonFrame__, text=button,  font=("Arial", 12),height=height, width=width * 2 + 1, justify="center", background="blue",
                       fg="white", activeforeground="skyblue",
                       command=lambda __value__=button: self.__buttonClick__(__value__)).grid(row=self.__rowValue__+1,
                                                                                              column=1,columnspan = 2 )
            elif button == "Exit":
                Button(self.__exitFrame__, text="Exit", command=self.__root__.destroy, fg="BLUE", background="lightblue", justify="left",
                       width=7, relief="groove", anchor="center", font=("Arial",10)).grid(row=self.__rowValue__, column=1, columnspan=2)
            elif button == "Settings":
                Button(self.__buttonFrame__, text=button, font=("Arial", 12), height=height, width=width, justify="center", background="blue",
                       fg="white", activeforeground="skyblue",
                       command=self.settingsCallback).grid(row=self.__rowValue__ +1, column=3)

            else:
                if self.__columnValue__ & 3 == 0:
                    self.__rowValue__ += 1
                    self.__columnValue__ = 1
                Button(self.__buttonFrame__, font=("Arial", 12), text=button, height=3, width=width, justify="center", background="blue", fg="white", activeforeground="skyblue",
                       command=lambda __value__ = button:self.__buttonClick__(__value__)).grid(row=self.__rowValue__,column=self.__columnValue__)
                self.__columnValue__ +=1



    def __buttonClick__(self,value):

        self.__clickValue__ = value
        if self.__clickValue__ not in "+-*/C" and (self.__clickValue__ != "Exit" and self.__clickValue__ != "Settings"):
            self.__operand__  = self.__operand__+self.__clickValue__
            self.entry.delete(0,END)
            self.entry.insert(0,self.__operand__)
        elif self.__clickValue__ in "*/+-":
            self.__operator__ = self.__clickValue__
            self.operand_1 = self.entry.get()
            self.entry.delete(0, END)
            self.entry.insert(0, self.__operator__)
        elif  self.__clickValue__ == "C":
            self.resetOperands()
            self.result = None

    def displayPreviousResult(self,__value__):
        self.__value__ = __value__
        if self.__value__:
            self.entry.delete(0,END)
            self.entry.insert(0,f"{self.operandExpression}")
        else:
            self.entry.delete(0,END)


    def solve(self):
        self.operand_2 = self.entry.get()
        self.entry.delete(0, END)
        self.operandExpression  = f"{self.operand_1}{self.operator}{self.operand_2}"
        self.__result__ = eval(self.operandExpression)

    def resetOperands(self):
        self.operand_1 = None
        self.operand_2 = None
        self.__operand__ = ""
        self.__result__ = None
        self.operandExpression = None

    def metaLabel(self):
        self.getState = IntVar()
        Label(self.__metaFrameHandler__,text="Ibraztech", fg="blue").grid(row=0,column=0)
        Label(self.__metaFrameHandler__,text="  ", fg="blue").grid(row=0,column=1)
        if self.__result__ == None:
            Checkbutton(self.__metaFrameHandler__, justify="center", command=lambda value=self.getState:self.displayPreviousResult(value),
                        onvalue=True, offvalue=False,text="Previous Solution",state="disabled")#activebackground=,activeforeground=,background=)
        else:
            Checkbutton(self.__metaFrameHandler__, justify="center", command=lambda value=self.getState:self.displayPreviousResult(value),
                        onvalue=True, offvalue=False,text="Previous Solution",state="active")#activebackground=,activeforeground=,background=)
        Label(self.__metaFrameHandler__,text="  ", fg="blue").grid(row=0,column=2)
        Label(self.__metaFrameHandler__,text="Meta", fg="blue").grid(row=0,column=3)

    def settingsCallback(self):
        pass


    def __frameHandler__(self):
        self.__mainCalculatorWidget__ = Label(self.__root__,background="lightblue")
        self.entry = Entry(self.__mainCalculatorWidget__,justify="left",width=40)
        self.__buttonFrame__ = Label(self.__mainCalculatorWidget__, bg="skyblue")
        self.__metaFrameHandler__ = Label(self.__mainCalculatorWidget__)
        self.__exitFrame__ = Label(self.__mainCalculatorWidget__,background="lightblue")

    def __gridHandlerAndMainloop__(self):
        self.__mainCalculatorWidget__.grid(row=0,column=0)

        #main Calculator widget child Class
        self.entry.grid(row=0,column=0)
        self.__metaFrameHandler__.grid(row=1, column=0)
        self.__buttonFrame__.grid(row=2, column=0)
        self.__exitFrame__.grid(row=3,column=0)

        self.__root__.mainloop()

    def activate(self):
        self.__frameHandler__()
        self.__gridHandlerAndMainloop__()
        self.__displayButton__()






from tkinter import *

calculator = Calculator()
calculator.activate()
