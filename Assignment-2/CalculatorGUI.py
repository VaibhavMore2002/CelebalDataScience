import tkinter as tk


def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Clear":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


window = tk.Tk()
window.title("Calculator - Made By Vaibhav")

entry = tk.Entry(window, relief=tk.SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'Clear', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    b = tk.Button(window, text=button, width=5, height=2)
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    b.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
window.mainloop()
