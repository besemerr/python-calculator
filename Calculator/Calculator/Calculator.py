from tkinter import *

root = Tk()
root.wm_iconbitmap("C:\\Users\\rbesemer\\PycharmProjects\\pythonProject\\Calculator\\images\\Paomedia-Small-N-Flat"
                "-Calculator.ico")
root.title("Calculator")
root.configure(bg="black")
root.resizable(width=False, height=False)
operands = ['÷', 'x', '-', '+']
math = ""
last_answer = ""


def value_check(value):
    for item in operands:
        if value == str(item) or value.isnumeric():
            return value


def duplicate_check(last_value, current_value):
    for item in operands:
        if last_value == current_value and item == current_value and item == last_value:
            return True


def operand_replace(value):
    value = value.replace('÷', '/')
    value = value.replace('x', '*')
    return value


def float_check(value):
    value = operand_replace(value)
    check = calculate(str(value).replace('/', '%'))
    if check == 0:
        value = calculate(str(value).replace('%', '/'))
        return int(value)
    else:
        value = calculate(str(value).replace('%', '/'))
        return value


def calculate(equation):
    answer = eval(equation)
    return answer


def clear():
    s1.delete(0, END)
    s2.delete(0, END)


def equals():
    global math
    global last_answer
    s1.delete(0, END)
    s1.insert(0, s2.get())
    s2.delete(0, END)
    math = "equals"
    last_answer = s1.get()


def key_pressed(event, caller):
    global math
    global last_answer
    if caller == "root":
        event_val = event.char
        cmd = event.keysym
        if event_val == '/':
            event_val = '÷'
        if event_val == '*':
            event_val = 'x'
    else:
        event_val = event
        cmd = ""
    if math == "equals":
        if event_val == operands[0] or event_val == operands[1] or event_val == operands[2] or event_val == operands[3]:
            clear()
            s1.insert(0, last_answer)
            math = ""
        else:
            clear()
            math = ""
    value = value_check(event_val)
    duplicate = False
    if len(s1.get()) > 1:
        duplicate = duplicate_check(s1.get()[len(s1.get()) - 1], event_val)
    escape = "Escape"
    enter = "Return"
    if value is not None:
        if not duplicate:
            current = s1.get()
            s1.delete(0, END)
            s1.insert(0, current + str(value))
            operand = False
            for item in operands:
                if s1.get()[len(s1.get()) - 1] == item:
                    current_answer = float_check(s1.get()[:-1])
                    s2.insert(0, current_answer)
                    operand = True
                else:
                    s2.delete(0, END)
            if len(s1.get()) > 2 and not operand:
                try:
                    current_answer = float_check(s1.get())
                    s2.delete(0, END)
                    s2.insert(0, current_answer)
                except ZeroDivisionError:
                    s1.delete(0, END)
                    s1.insert(0, "Cannot Divide by Zero")
                    math = "equals"
    elif cmd == escape:
        clear()
    elif cmd == enter:
        equals()


root.bind("<Key>", lambda event: key_pressed(event, "root"))

# declare entry screens
s1 = Entry(root, text="", width=16, bg='black', fg='white', borderwidth=0, font=('Times\\New\\Roman 34 bold'), justify='right')
s2 = Entry(root, text="", width=33, bg='black', fg='gray30', borderwidth=0, font=('Times\\New\\Roman 16 bold'), justify='right')

# place entry screens on the grid
s1.grid(row=0, column=0, columnspan=4)
s2.grid(row=1, column=0, columnspan=4)

# declare the buttons
button_1 = Button(root, text="1", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('1', "button"))
button_2 = Button(root, text="2", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('2', "button"))
button_3 = Button(root, text="3", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('3', "button"))
button_4 = Button(root, text="4", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('4', "button"))
button_5 = Button(root, text="5", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('5', "button"))
button_6 = Button(root, text="6", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('6', "button"))
button_7 = Button(root, text="7", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('7', "button"))
button_8 = Button(root, text="8", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('8', "button"))
button_9 = Button(root, text="9", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('9', "button"))
button_0 = Button(root, text="0", width=3, bg="gray5", fg="white", font=('default 36 bold'), command=lambda: key_pressed('0', "button"))
button_add = Button(root, text="+", width=3, bg="gray5", fg="green", font=('default 36 bold'), command=lambda: key_pressed('+', "button"))
button_sub = Button(root, text="-", width=3, bg="gray5", fg="green", font=('default 36 bold'), command=lambda: key_pressed('-', "button"))
button_multi = Button(root, text="x", width=3, bg="gray5", fg="green", font=('default 36 bold'), command=lambda: key_pressed('x', "button"))
button_div = Button(root, text="÷", width=3, bg="gray5", fg="green", font=('default 36 bold'), command=lambda: key_pressed('÷', "button"))
button_equals = Button(root, text="=", width=3, bg="green", fg="white", font=('default 36 bold'), command=equals)
button_clear = Button(root, text="C", width=3, bg="gray5", fg="red", font=('default 36 bold'), command=clear)

# place buttons on the grid
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_clear.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equals.grid(row=5, column=2)

button_add.grid(row=5, column=3)
button_sub.grid(row=4, column=3)
button_multi.grid(row=3, column=3)
button_div.grid(row=2, column=3)

root.mainloop()
