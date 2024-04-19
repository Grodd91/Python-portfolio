import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(root, text=button, width=5, command=lambda btn=button: self.on_button_click(btn)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error!")
        elif value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '√':
            try:
                number = float(self.entry.get())
                result = math.sqrt(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error!")
        elif value == 'sin':
            try:
                angle = float(self.entry.get())
                result = math.sin(math.radians(angle))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error!")
        elif value == 'cos':
            try:
                angle = float(self.entry.get())
                result = math.cos(math.radians(angle))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error!")
        else:
            self.entry.insert(tk.END, value)

root = tk.Tk()
calculator = AdvancedCalculator(root)
root.mainloop()
