import math
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("LSWQ Calculator")
root.geometry("400x500")  # Set window size

# Create a StringVar to store the input
user_input = tk.StringVar()

# Function to update input field
def update_input(value):
    current_text = user_input.get()  # Get current input
    user_input.set(current_text + value)  # Append the pressed value

# Function to clear the input field
def clear_input():
    user_input.set("")  # Clear input

# Function for addition
def sum_nums(num1, num2):
    return num1 + num2

# Function for subtraction
def sub_nums(num1, num2):
    return num1 - num2

# Function for division
def divide_nums(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

# Function for multiplication
def multiply_nums(num1, num2):
    return num1 * num2

# Function to evaluate the expression and display the result
def calculate():
    try:
        expression = user_input.get()  # Get the input string from the entry field

        # Identify and split based on the operator
        if '+' in expression:
            num1, num2 = map(float, expression.split('+'))
            result = sum_nums(num1, num2)
        elif '-' in expression:
            num1, num2 = map(float, expression.split('-'))
            result = sub_nums(num1, num2)
        elif '*' in expression:  # Multiplication operator
            num1, num2 = map(float, expression.split('*'))
            result = multiply_nums(num1, num2)
        elif '/' in expression:
            num1, num2 = map(float, expression.split('/'))
            result = divide_nums(num1, num2)
        else:
            result = "Error"  # Handle invalid operations

        # Display the result
        user_input.set(str(result))
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the input field (entry widget)
input_field = tk.Entry(root, textvariable=user_input, font=("Arial", 24), justify="right", bd=10)
input_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Modify the button creation logic for special handling of '='
def create_button(text, row, column, command=None):
    if not command:
        command = lambda: update_input(text)  # Default command to update input field
    if text == '=':  # Special handling for '='
        command = calculate
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=command)
    button.grid(row=row, column=column, padx=10, pady=10)

# Create calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),  # Note that 'x' will be replaced with '*' for multiplication
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons dynamically
for (text, row, column) in buttons:
    create_button(text, row, column)

# Special buttons
create_button('C', 5, 0, command=clear_input)  # Clear button
create_button('=', 5, 3, command=calculate)  # Equals button to perform the calculation

# Replace "x" button for multiplication to use '*'
create_button('x', 2, 3, command=lambda: update_input('*'))

# Run the main loop
root.mainloop()
