import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Помилка")

# Головне вікно
root = tk.Tk()
root.title("Простий Калькулятор")

# Встановлення мінімального та максимального розмірів вікна
root.minsize(300, 400)
root.maxsize(600, 800)

# Поле для введення
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки чисел
buttons = [
    tk.Button(root, text=str(i), padx=20, pady=20, font=("Arial", 14), command=lambda i=i: button_click(i))
    for i in range(10)
]

# Розташування кнопок чисел
buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)

buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)

buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)

buttons[0].grid(row=4, column=0)

# Кнопки операцій
button_add = tk.Button(root, text="+", padx=20, pady=20, font=("Arial", 14), command=lambda: button_click("+"))
button_sub = tk.Button(root, text="-", padx=20, pady=20, font=("Arial", 14), command=lambda: button_click("-"))
button_mul = tk.Button(root, text="*", padx=20, pady=20, font=("Arial", 14), command=lambda: button_click("*"))
button_div = tk.Button(root, text="/", padx=20, pady=20, font=("Arial", 14), command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=45, pady=20, font=("Arial", 14), command=button_equal)
button_clear = tk.Button(root, text="C", padx=45, pady=20, font=("Arial", 14), command=button_clear)

# Розташування кнопок операцій
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

# Запуск програми
root.mainloop()
