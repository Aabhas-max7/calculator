import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("450x350")
window.configure(bg="#2b2b2b")
window.resizable(False, False)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=20)
entry_frame.config(bg="#2b2b2b")

entry = tk.Entry(entry_frame, bg="white", fg="black", borderwidth = 2, font = ("Arial", 14), width = 25, relief = "solid")
entry.grid(row = 0, column = 0, padx = 10, pady = 10)

button_frame = tk.Frame(window)
button_frame.pack()
button_frame.config(bg="#2b2b2b")

def button_clicked(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

num_btn_style = {
    "bg": "#d4d4d4",
    "fg": "black",
    "activebackground": "#bfbfbf",
    "font": ("Arial", 12, "bold")
}

button1 = tk.Button(button_frame, text = "1", width = 5, height = 2, command = lambda: button_clicked(1), **num_btn_style,cursor="hand2")
button1.grid(row = 1, column = 0, padx = 5, pady = 5,)

button2 = tk.Button(button_frame, text = "2", width = 5, height = 2, command = lambda: button_clicked(2), **num_btn_style,cursor="hand2")
button2.grid(row = 1, column = 1, padx = 5, pady = 5)

button3 = tk.Button(button_frame, text = "3", width = 5, height = 2, command = lambda: button_clicked(3), **num_btn_style,cursor="hand2")
button3.grid(row = 1, column = 2, padx = 5, pady = 5)

button4 = tk.Button(button_frame, text = "4", width = 5, height = 2, command = lambda: button_clicked(4), **num_btn_style,cursor="hand2")
button4.grid(row = 2, column = 0, padx = 5, pady = 5)

button5 = tk.Button(button_frame, text = "5", width = 5, height = 2, command = lambda: button_clicked(5), **num_btn_style,cursor="hand2")
button5.grid(row = 2, column = 1, padx = 5, pady = 5)

button6 = tk.Button(button_frame, text = "6", width = 5, height = 2, command = lambda: button_clicked(6), **num_btn_style,cursor="hand2")
button6.grid(row = 2, column = 2, padx = 5, pady = 5)

button7 = tk.Button(button_frame, text = "7", width = 5, height = 2, command = lambda: button_clicked(7), **num_btn_style,cursor="hand2")
button7.grid(row = 3, column = 0, padx = 5, pady = 5)

button8 = tk.Button(button_frame, text = "8", width = 5, height = 2, command = lambda: button_clicked(8), **num_btn_style,cursor="hand2")
button8.grid(row = 3, column = 1, padx = 5, pady = 5)

button9 = tk.Button(button_frame, text = "9", width = 5, height = 2, command = lambda: button_clicked(9), **num_btn_style,cursor="hand2")
button9.grid(row = 3, column = 2, padx = 5, pady = 5)

button0 = tk.Button(button_frame, text = "0", width = 5, height = 2, command = lambda: button_clicked(0), **num_btn_style,cursor="hand2")
button0.grid(row = 4, column = 1, padx = 5, pady = 5)

def add_operator(op):
    entry.insert(tk.END, op)

op_btn_style = {
    "bg": "#ff9500",
    "fg": "white",
    "activebackground": "#e08600",
    "font": ("Arial", 12, "bold")
}

btn_plus = tk.Button(button_frame, text = "+", width = 5, height = 2, command = lambda: add_operator("+"), **op_btn_style,cursor="hand2")
btn_plus.grid(row = 1, column = 3, padx = 5, pady = 5)

btn_minus = tk.Button(button_frame, text = "-", width = 5, height = 2, command = lambda: add_operator("-"), **op_btn_style,cursor="hand2")
btn_minus.grid(row = 2, column = 3, padx = 5, pady = 5)

btn_mul = tk.Button(button_frame, text = "*", width = 5, height = 2, command = lambda: add_operator("*"), **op_btn_style,cursor="hand2")
btn_mul.grid(row = 3, column = 3, padx = 5, pady = 5)

btn_div = tk.Button(button_frame, text = "/", width = 5, height = 2, command = lambda: add_operator("/"), **op_btn_style,cursor="hand2")
btn_div.grid(row = 4, column = 2, padx = 5, pady = 5)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")

btn_eql = tk.Button(button_frame, text = "=",bg="#34c759", fg="white", activebackground="#2fa94f",font=("Arial", 12, "bold"), width = 5, height = 2, command = calculate)
btn_eql.grid(row = 4, column = 3, padx = 5, pady = 5)

def clear():
    entry.delete(0, tk.END)

btn_clear = tk.Button(button_frame, text = "C", bg="#ff3b30", fg="white",activebackground="#d63027",font=("Arial", 12, "bold"), width = 5, height = 2, command = clear)
btn_clear.grid(row = 4, column = 0, padx = 5, pady = 5)

window.mainloop()