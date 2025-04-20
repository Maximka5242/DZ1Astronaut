import tkinter as tk
from tkinter import messagebox

# Функція для додавання символів до поля введення
def button_click(value):
    entry_field.insert(tk.END, value)

# Функція для обчислення виразу
def calculate():
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))

# Функція для очищення поля введення
def clear():
    entry_field.delete(0, tk.END)

# Створення головного вікна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("265x425")
root.minsize(265, 425)
root.maxsize(265, 425)

# Поле введення
entry_field = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry_field.grid(row=0, column=0, columnspan=4)

# Кнопки калькулятора
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('^', 5, 0), ('(', 5, 1), (')', 5, 2), ('=', 5, 3),
]

# Додавання кнопок до вікна
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightblue", command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightcoral", command=clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda value=text: button_click(value))
    btn.grid(row=row, column=col, sticky="nsew")




# Запуск головного циклу програми
root.mainloop()
