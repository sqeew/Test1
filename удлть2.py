from tkinter import *
from functools import partial

primer=''

def click(nameB):
    global primer
    if nameB == '=':
        primer=eval(primer)
        label.config(text=primer)
    elif nameB == 'C':
        primer =''
        label.config(text=primer)
    elif nameB == 'DEL':
        primer = primer[0:-1]
        label.config(text=primer)
    elif nameB == 'X^2':
        primer = primer+'**2'
        label.config(text = primer)
    else:
        primer += nameB
        label.config(text=primer)




root = Tk()

root.config(bg = "black")
root.geometry("485x550")
root.title("Калькулятор")
root.resizable(False, False)

label = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
label.place(x = 10, y = 50)

buttonNames = [
"C", "DEL", "*", "=",
"1", "2", "3", "/",
"4", "5", "6", "+", 
"7", "8", "9", "-",
"(", "0", ")", "X^2"
]

x=10
y=140

for i in buttonNames:
    Button(
        text=i,
        bg='white',
        font=('Consolas',15),
        command=partial(click,i)
        ).place(
            x=x,
            y=y,
            width = 115,
            height = 79)
    x+=117
    if x > 400:
        x=10
        y+=81

root.mainloop()
Button.mainloop()
