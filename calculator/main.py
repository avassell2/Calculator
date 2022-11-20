import tkinter as tk #module for graphical user interface

calculation = ""

def add_to_calc(symbol):
    global calculation #calculation is a globale variable so it can be be manipuated inside functions
    calculation += str(symbol) #adds to calculation string
    text_result.delete(1.0,"end") #1.0 is staring index so we delete full content of text result field
    text_result.insert(1.0, calculation)


def evaluate_calc():
    global calculation
    if '\u00b2' in calculation:
        calculation = str(calculation).replace('\u00b2', '**2')

    if '\u221a' in calculation:
        calculation = str(calculation).replace('\u221a', '**0.5')
        #square(calculation)
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")








root = tk.Tk()
root.geometry("300x275") #size of screen

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24)) # text field for results
text_result.grid(columnspan = 5)


#buttons

#numbers


btn_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

#operations

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_square = tk.Button(root, text="x\u00b2", command=lambda: add_to_calc("\u00b2"), width=5, font=("Arial", 14))
btn_square.grid(row=6, column=3)

btn_sqrt = tk.Button(root, text="\u221ax", command=lambda: add_to_calc("\u221a"), width=5, font=("Arial", 14))
btn_sqrt.grid(row=6, column=4)

#paranthese

btn_open = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)



btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1)

btn_equals = tk.Button(root, text="=", command= evaluate_calc, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=2)













root.mainloop()
