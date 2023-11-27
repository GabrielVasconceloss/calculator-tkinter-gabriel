import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator Gabriel")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val,
                                                                                                    column=col_val,
                                                                                                    sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure layout
        for i in range(1, 5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == '0' or self.result_var.get() == 'Error':
                self.result_var.set(value)
            else:
                self.result_var.set(self.result_var.get() + value)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    calculator = Calculator(root)
    root.mainloop()
