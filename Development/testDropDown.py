from tkinter import *

root = Tk()

# Chose Experiment or Production Mode
tkvar = StringVar(root)
choises = {"Production", "Experiment"}
tkvar.set("Production")
OperationMode = OptionMenu(root, tkvar,  *choises)
OperationMode.place(x=21, y=90)
OperationMode.config(relief = "sunken", bd= 0)
OperationMode.pack()

# Entry widget for operation mode comment
OperationModeInput = Entry(root, bd = '3' , relief = "sunken")
OperationModeInput.place(x=130, y=92)
OperationModeInput.pack()

def readNow():
	print(OperationMode.cget("text"))

button = Button(root, text = "OK", command=readNow)
button.pack()

mainloop()
