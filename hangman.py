import tkinter as tk
from PIL import Image, ImageTk
import random


IMG_WIDTH = 500
IMG_HEIGHT = 300

# create hangman app
frame = tk.Tk()
frame.title = "Hangman Game"

hangman_pic = tk.Label(master=frame)
hm_pic = Image.open("./asset/hang1.png")
hm_pic = hm_pic.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
hm_pic = ImageTk.PhotoImage(hm_pic)
hangman_pic.config(image=hm_pic)
hangman_pic.img = hm_pic

text = tk.Label(master=frame, font=("Arial", 25), relief=tk.RAISED)

label = tk.Label(master=frame, font=("Arial", 25))
button = tk.Button(master=frame)

# global variable
pic = 1
fullword = ""

def main():
    global frame, hangman_pic, text, fullword
    
    fullword = setText()
    print(fullword)
    
    w = ""
    for _ in fullword:
        w += "_ "
    text.config(text=w)
    
    hangman_pic.pack()
    text.pack()
    
    frame.bind("<Key>", key_pressed)
    frame.mainloop()

def changePic():
    global frame, pic, hangman_pic, text
    pic += 1;
    if(pic == 1): img = Image.open("./asset/hang1.png") 
    elif(pic == 2): img = Image.open("./asset/hang2.png") 
    elif(pic == 3): img = Image.open("./asset/hang3.png") 
    elif(pic == 4): img = Image.open("./asset/hang4.png") 
    elif(pic == 5): img = Image.open("./asset/hang5.png") 
    elif(pic == 6): img = Image.open("./asset/hang6.png") 
    elif(pic == 7): img = Image.open("./asset/hang7.png") 
    else: 
        text.config(text=fullword)
        lose()
    img = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    hangman_pic.config(image=img)
    hangman_pic.img = img  

def setText():
    with open("word.txt", "rt") as f:
        words = f.read().split("\n")
    word = random.choice(words)
    return word

def key_pressed(event):
    global fullword, text
    if(event.char in fullword):
        w = ""
        cur_text = text.cget("text")
        for i in range(len(fullword)):
            if event.char == fullword[i] or fullword[i] in cur_text: w += fullword[i] + " "
            else: w += "_ "
        text.config(text=w)
        if(w.replace(" ", "") == fullword):
            win()
    else:
        changePic()

def win():
    print("Win")
    global label, button, frame
    label.config(text="Congratualtion")
    button.config(text="Play Again", command=restart)
    label.pack()
    button.pack()
    frame.unbind("<Key>")

def lose():
    print("Lose")
    global label, button, frame
    label.config(text="You Lose")
    button.config(text="Play Again", command=restart)
    label.pack()
    button.pack()
    frame.unbind("<Key>")

def restart():
    global text, hangman_pic, frame, fullword, pic, label, button
    pic = 0
    fullword = setText()
    w = ""
    for _ in fullword:
        w += "_ "
    text.config(text=w)
    changePic()
    label.pack_forget()
    button.pack_forget()
    frame.bind("<Key>", key_pressed)
    print(fullword)

if __name__ == '__main__':
    main()