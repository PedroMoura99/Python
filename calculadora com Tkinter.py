from tkinter import *
 
class Calculator:
    def __init__(self, parent):
 
        #Valores
        self.n1 = ''
        self.operation = ''
        self.n2 = ''
 
 
 
        #Janela
        self.myParent = parent
        self.myParent.title('Calculadora')
        self.myParent.geometry('210x480')
        self.myParent.resizable(0,0)
 
        self.myContainer0 = Frame(parent)
        self.myContainer0.pack()
 
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
 
        self.myContainer2 = Frame(parent)
        self.myContainer2.pack()
 
        self.myContainer3 = Frame(parent)
        self.myContainer3.pack()
 
        self.myContainer4 = Frame(parent)
        self.myContainer4.pack()
 
        self.myContainer5 = Frame(parent)
        self.myContainer5.pack()
 
 
 
        #Visores
        self.visorValue1 = Label(self.myContainer0)
        self.visorValue1.configure(background="#FFFFFF",height=5,width=5,text=self.n1)
        self.visorValue1.pack(side=LEFT)
 
        self.visorOperation = Label(self.myContainer0)
        self.visorOperation.configure(background="#FFFFFF",height=5,width=1,text=self.operation)
        self.visorOperation.pack(side=LEFT)
 
        self.visorValue2 = Label(self.myContainer0)
        self.visorValue2.configure(background="#FFFFFF",height=5,width=5,text=self.n2)
        self.visorValue2.pack(side=LEFT)
 
        self.visorEquals = Label(self.myContainer0)
        self.visorEquals.configure(background="#FFFFFF",height=5,width=1,text='')
        self.visorEquals.pack(side=LEFT)
 
        self.visorResult = Label(self.myContainer0)
        self.visorResult.configure(background="#FFFFFF",height=5,width=14,text='')
        self.visorResult.pack(side=LEFT)
 
 
 
        #Botões de valor
        self.button1 = Button(self.myContainer1, command=self.button1Click)  ### (1)
        self.button1.configure(height=5,width=6,text="1", background="#FF9933")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()
 
 
        self.button2 = Button(self.myContainer1, command=self.button2Click)  ### (2)
        self.button2.configure(height=5,width=6,text="2", background="#FF9933")
        self.button2.pack(side=LEFT)
        self.button2.focus_force()
 
 
        self.button3 = Button(self.myContainer1, command=self.button3Click)  ### (3)
        self.button3.configure(height=5,width=6,text="3", background="#FF9933")
        self.button3.pack(side=LEFT)
        self.button3.focus_force()
 
 
        self.button4 = Button(self.myContainer2, command=self.button4Click)  ### (4)
        self.button4.configure(height=5,width=6,text="4", background="#FF9933")
        self.button4.pack(side=LEFT)
        self.button4.focus_force()
 
 
        self.button5 = Button(self.myContainer2, command=self.button5Click)  ### (5)
        self.button5.configure(height=5,width=6,text="5", background="#FF9933")
        self.button5.pack(side=LEFT)
        self.button5.focus_force()
 
        self.button6 = Button(self.myContainer2, command=self.button6Click)  ### (6)
        self.button6.configure(height=5,width=6,text="6", background="#FF9933")
        self.button6.pack(side=LEFT)
        self.button6.focus_force()
 
        self.button7 = Button(self.myContainer3, command=self.button7Click)  ### (7)
        self.button7.configure(height=5,width=6,text="7", background="#FF9933")
        self.button7.pack(side=LEFT)
        self.button7.focus_force()
 
        self.button8 = Button(self.myContainer3, command=self.button8Click)  ### (8)
        self.button8.configure(height=5,width=6,text="8", background="#FF9933")
        self.button8.pack(side=LEFT)
        self.button8.focus_force()
 
        self.button9 = Button(self.myContainer3, command=self.button9Click)  ### (9)
        self.button9.configure(height=5,width=6,text="9", background="#FF9933")
        self.button9.pack(side=LEFT)
        self.button9.focus_force()
 
        self.pointButton = Button(self.myContainer4,command=self.buttonPointClick)
        self.pointButton.configure(height=5,width=6,text=".", background="#FF9933")
        self.pointButton.pack(side=LEFT)
        self.pointButton.focus_force()
 
        self.button0 = Button(self.myContainer4, command=self.button0Click)  ### (0)
        self.button0.configure(height=5,width=6,text="0", background="#FF9933")
        self.button0.pack(side=LEFT)
        self.button0.focus_force()
 
 
 
 
        ##Botões de operação
        self.buttonReset = Button(self.myContainer5,command=self.ResetClick)                     ##Reset
        self.buttonReset.configure(height=3,width=28,text="RESET",background="#FF9933")
        self.buttonReset.pack(side=LEFT)
        self.buttonReset.focus_force()
 
        self.buttonAddition = Button(self.myContainer1,command=self.AdditionClick)               ##Addition
        self.buttonAddition.configure(height=5,width=6,text="+",background="#FF9933")
        self.buttonAddition.pack(side=LEFT)
        self.buttonAddition.focus_force()
 
        self.buttonSubtraction = Button(self.myContainer2,command=self.SubtractionClick)         ##Subtraction
        self.buttonSubtraction.configure(height=5,width=6,text="-",background="#FF9933")
        self.buttonSubtraction.pack(side=LEFT)
        self.buttonSubtraction.focus_force()
 
        self.buttonMultiplication = Button(self.myContainer3,command=self.MultiplicationClick)  ##Multiplication
        self.buttonMultiplication.configure(height=5,width=6,text="*",background="#FF9933")
        self.buttonMultiplication.pack(side=LEFT)
        self.buttonMultiplication.focus_force()
 
        self.buttonEquals = Button(self.myContainer4,command=self.Equals)                       ##Equals
        self.buttonEquals.configure(height=5,width=6,text="=",background="#FF9933")
        self.buttonEquals.pack(side=LEFT)
        self.buttonEquals.focus_force()
 
        self.buttonDivision = Button(self.myContainer4,command=self.DivisionClick)              ##Division
        self.buttonDivision.configure(height=5,width=6,text="/", background="#FF9933")
        self.buttonDivision.pack(side=LEFT)
        self.buttonDivision.focus_force()
 
 
 
 
    ##Funções
    def button1Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '1'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '1'
            self.visorValue2.configure(text=self.n2)
 
    def button2Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '2'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '2'
            self.visorValue2.configure(text=self.n2)
 
    def button3Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '3'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '3'
            self.visorValue2.configure(text=self.n2)
 
    def button4Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '4'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '4'
            self.visorValue2.configure(text=self.n2)
 
    def button5Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '5'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '5'
            self.visorValue2.configure(text=self.n2)
 
    def button6Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '6'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '6'
            self.visorValue2.configure(text=self.n2)
 
    def button7Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '7'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '7'
            self.visorValue2.configure(text=self.n2)
 
    def button8Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '8'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '8'
            self.visorValue2.configure(text=self.n2)
 
    def button9Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '9'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '9'
            self.visorValue2.configure(text=self.n2)
 
    def button0Click(self):
        if self.operation == '':
            self.n1 = self.n1 + '0'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '0'
            self.visorValue2.configure(text=self.n2)
 
    def buttonPointClick(self):
        if self.operation == '':
            self.n1 = self.n1 + '.'
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + '.'
            self.visorValue2.configure(text=self.n2)
 
    def AdditionClick(self):
        self.operation="+"
        self.visorOperation.configure(text=self.operation)
 
    def SubtractionClick(self):
        self.operation="-"
        self.visorOperation.configure(text=self.operation)
 
    def MultiplicationClick(self):
        self.operation="*"
        self.visorOperation.configure(text=self.operation)
 
    def DivisionClick(self):
        self.operation="/"
        self.visorOperation.configure(text=self.operation)
 
    def Equals(self):
        if self.operation=='':
            pass
        if self.operation=='+':
            self.visorResult.configure(text="%.2f"%(float(self.n1) + float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='-':
            self.visorResult.configure(text="%.2f"%(float(self.n1) - float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='*':
            self.visorResult.configure(text="%.2f"%(float(self.n1) * float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='/':
            if float(self.n2)==0:
                self.visorValue1.configure(text='Math')
                self.visorValue2.configure(text='Error')
                self.visorResult.configure(text='Try Again')
                self.n1=''
                self.operation=''
                self.n2=''
            else:
                self.visorResult.configure(text="%.2f"%(float(self.n1) / float(self.n2)))
                self.visorEquals.configure(text="=")
 
    def ResetClick(self):
        self.n1=''
        self.n2=''
        self.operation=''
        self.visorValue1.configure(text=self.n1)
        self.visorValue2.configure(text=self.n2)
        self.visorOperation.configure(text=self.operation)
        self.visorResult.configure(text='')
 
 
root = Tk()
myapp = Calculator(root)
root.mainloop()
