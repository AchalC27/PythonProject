from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from words import *

window = Tk()
window.title('Hangman')
window.geometry('450x600')
window.configure(bg='LightBlue')  

photos = [PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang0.png").subsample(4), PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang1.png").subsample(4),PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang2.png").subsample(4), 
        PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang3.png").subsample(4),PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang4.png").subsample(4), PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang5.png").subsample(4),
        PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang6.png").subsample(4), PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang7.png").subsample(4),PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang8.png").subsample(4), 
        PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang9.png").subsample(4),PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang10.png").subsample(4), PhotoImage(file="D:/Python/HangMan/PythonProject/images/hang11.png").subsample(4)]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    word = random.choice(word_list)
    word = word.upper()
    the_word_withSpaces = " ".join(word)
    lblWord.set(' '.join("_" * len(word)))
    imgLabel.config(image=photos[0])  

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
                    animate_win()
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            window.update_idletasks()  
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over")
                animate_loss()

animation_speed = 100  
current_frame = 0
def animate_win():
    global current_frame
    for i in range(1, 12):
        imgLabel.config(image=photos[i % 12])
        window.update_idletasks()
        window.after(animation_speed)
        current_frame = i

def animate_loss():
    global current_frame
    for i in range(current_frame, 12):
        imgLabel.config(image=photos[i % 12])
        window.update_idletasks()
        window.after(animation_speed)

def on_key(event):
    key = event.char.upper()
    if key.isalpha():
        guess(key)

imgLabel = Label(window, bg='LightBlue')
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lblWord = StringVar()
Label(window, textvariable=lblWord, font=('consolas 24 bold'), bg='LightBlue', fg='blue4').place(x=200, y=100)

n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18', 15), width=6, height=2, bg='Gold1').grid(row=1 + n // 6, column=n % 6)
    n += 1

Button(window, text="New Game", command=lambda: newGame(), font=("Helvetica 10 bold"),width=20,height=2, activebackground='goldenrod4',activeforeground='white', bg='Gold1').grid(row=5, column=2, columnspan=3, pady=10)

newGame()

window.bind("<Key>", on_key)
window.mainloop()
