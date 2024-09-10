import tkinter as tk

class Calculator:
    def _init_(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Calculator")

        # Create entry field for display
        self.entry_field = tk.Entry(self.window, width=40, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=4)  # Adjust columnspan to control the width

        # Create buttons for digits and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        # Loop to create each button
        for button in buttons:
            tk.Button(self.window, text=button, width=10, height=3, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    # Handle button clicks
    def click_button(self, button):
        if button == '=':
            try:
                # Evaluate the expression in the entry field
                result = eval(self.entry_field.get())
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            # Append the clicked button value to the entry field
            self.entry_field.insert(tk.END, button)

    # Run the main loop of the calculator
    def run(self):
        self.window.mainloop()

# Create and run the calculator
if _name_ == "_main_":
    calculator = Calculator()
    calculator.run()
