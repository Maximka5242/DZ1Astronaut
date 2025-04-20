import tkinter as tk

# Initial game variables
bomb = 100
score = 0
press_return = True

# Create the main window
root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
root.iconbitmap("bomb.ico")

# Labels
label = tk.Label(root, text="Press [Enter] to start game", font=("Comic Sans MS", 12))
label.pack()

fuse_label = tk.Label(root, text=f"Fuse: {str(bomb)}", font=("Comic Sans MS", 14))
fuse_label.pack()

score_label = tk.Label(root, text=f"Score: {str(score)}", font=("Comic Sans MS", 14))
score_label.pack()

# Load images
img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")

bomb_label = tk.Label(root, image=img_2)
bomb_label.pack()

# Update display
def update_display():
    global bomb, score
    if bomb >= 80:
        bomb_label.config(image=img_1)
    elif 50 <= bomb < 80:
        bomb_label.config(image=img_2)
    elif 0 < bomb < 50:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)

    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(score))
    fuse_label.after(100, update_display)

# Check if the bomb is alive
def is_alive():
    global bomb, press_return
    if bomb <= 0:
        bomb = 0
        label.config(text="Bang! Bang! Bang!")
        press_return = True
        return False
    return True

# Decrease the bomb's fuse
def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(1000, update_bomb)

# Increase the score
def update_score():
    global score
    if is_alive():
        score += 3
        score_label.after(3000, update_score)

# Start the game
def start(event):
    global press_return, score, bomb
    if not press_return:
        return
    bomb = 100
    score = 0
    update_bomb()
    update_score()
    update_display()
    label.config(text="")
    press_return = False

# Increase the bomb fuse on click
def click(event=None):
    global bomb
    if is_alive():
        bomb += 1

# Bind click to button and key "S/s"
def clickS(event):
    click()

# Button for clicking
click_button = tk.Button(root, text="Click me", bg="black", fg="white", width=15,
                         font=("Comic Sans MS", 14), command=click)
click_button.pack()

# Bind keys
root.bind("<Return>", start)
root.bind("S", clickS)
root.bind("s", clickS)

# Mainloop
root.mainloop()
