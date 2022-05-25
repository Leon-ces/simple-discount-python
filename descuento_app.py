import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class discountCalculator(object):
    @staticmethod
    def discountApply(price, discount):
        return price* (1 - discount/100)

# Class that creates widgets and handles eventas
class converterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Field Options
        options = {'padx': 5, 'pady': 5}

        # Price & Discount Label
        self.price_label = ttk.Label(self, text="Price")
        self.price_label.grid(column=0, row=0, sticky=tk.W, **options)

        self.discount_label = ttk.Label(self, text="Discount %")
        self.discount_label.grid(column=0, row=1, sticky=tk.W, **options)

        # Price & Discount Entry
        self.price = tk.StringVar()
        self.price_entry = ttk.Entry(self, textvariable=self.price)
        self.price_entry.grid(column=1, row=0, **options)
        self.price_entry.focus()

        self.discount = tk.StringVar()
        self.discount_entry = ttk.Entry(self, textvariable=self.discount)
        self.discount_entry.grid(column=1, row=1, **options)

        # Button that applies the discountApply function from discountCalculator

        self.apply_button = ttk.Button(self, text="Apply")
        self.apply_button['command'] = self.calculate
        self.apply_button.grid(column=1, row=2)

        # Result Label
        self.result_label = ttk.Label(self)
        self.result_label.grid(column=1, row=3, **options)

        # add padding and show it. FUUUUCK dude why did it take me so long
        # to realize I forgot this. SHIT. I might be retarded
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def calculate(self):
        try:
            price = float(self.price_entry.get())
            discount = float(self.discount_entry.get())

            amount = discountCalculator.discountApply(price, discount)

            result = f'{amount} is the final price'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Discount Calculator")
        self.geometry("300x150")

if __name__ == "__main__":
    app = App()
    converterFrame(app)
    app.mainloop()
