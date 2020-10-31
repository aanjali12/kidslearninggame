# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:24:13 2020

@author: ANJALI
"""

# -- coding: utf-8 --
"""
Created on Fri Oct 30 11:40:11 2020

@author: ANJALI
"""

from tkinter import *
from string import ascii_uppercase
import random
from tkinter import messagebox
import mysql.connector
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anj@2001"
    )

    mycs = mydb.cursor()

    mycs.execute("CREATE DATABASE game")
except:
    pass





mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anj@2001",
            database="game"
             )



mycs = mydb.cursor()

try:
    mycs.execute("CREATE TABLE kid (name VARCHAR(255),email VARCHAR(100), password VARCHAR(255),Gender VARCHAR(10),Country VARCHAR(33))")
except:#name,email,Password,Gender,Country
    pass



def home():
 global top2
 top2 = Tk()
 top2.geometry("500x500")
 top2.configure(bg="lightgreen")
 l1 = Label(top2, text="LET'S PLAY WITH FRUITS\nLET'S PLAY WITH FRUITS\nLET'S PLAY WITH FRUITS\n",
           font=("Helvetica 10 bold"), height=60, bg='green', fg='white')
 l1.place(x=0, y=0)
 l2 = Label(top2, text="FRUIT PLAY", font="bold", height=3, width=20, fg="green")
 l2.place(x=200, y=40)
 l3 = Label(top2, text="Instructions")
 l3.place(x=180, y=150)
 l4 = Label(top2, bg="lightgreen",
           text="You have to guess the name of a fruit in only 10 guesses\nif guessed true, you are genious otherwise\n keep trying as you could be genious!!")
 l4.place(x=175, y=180)
 b1 = Button(top2, bg="darkgreen", fg="white", text="START", command=start)
 b1.place(x=290, y=260)
 top2.mainloop()

def start():
    global window
    top2.iconify()

    window = Toplevel(top2)
    window.title("Learning Game")
    window.geometry("500x500")
    window.configure(bg='lightblue')
    lb = Label(window, text="FRUITPLAY", font='bold', height=2, width=17, fg="darkblue")
    lb.place(x=250, y=50)
    l1 = Label(window, text="LET'S PLAY WITH FRUITS\nLET'S PLAY WITH FRUITS\nLET'S PLAY WITH FRUITS\n",
               font=("Helvetica 10 bold"), height=60, bg='blue', fg='white')
    l1.place(x=0, y=0)
    b1 = Button(window, text="Login", height=3, width=12, bg='darkblue', fg='lightblue', command=signin)
    b1.place(x=240, y=200)
    b2 = Button(window, text="SignUp", height=3, width=12, bg='darkblue', fg='lightblue', command=signup)
    b2.place(x=360, y=200)
    window.mainloop()


def signin():
    window.destroy()
    global root2
    root2 = Toplevel(top2)
    root2.geometry('500x500')
    root2.title("Login Here")

    def login():
        try:


            mycs.execute("select* from kid where email=%s and Password=%s", (Email.get(), passw.get()))
            row = mycs.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and password")
            else:
                root2.destroy()
                game()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")

    passw = StringVar()
    Email = StringVar()
    label_0 = Label(root2, text="Login Here", bg="brown", fg="white", width=32, height=3, font=("bold", 20))
    label_0.place(x=0, y=0)

    label_1 = Label(root2, text="Email ID", width=20, font=("bold", 10))
    label_1.place(x=80, y=170)

    entry_1 = Entry(root2, textvar=Email, bd=5)
    entry_1.place(x=240, y=170)

    label_2 = Label(root2, text="Password", width=20, font=("bold", 10))
    label_2.place(x=68, y=230)

    entry_2 = Entry(root2, textvar=passw, bd=5)
    entry_2.place(x=240, y=230)
    Button(root2, text='Submit', width=20, bg='brown', fg='white', command=login).place(x=180, y=380)

    root2.mainloop()


def signup():
    global root
    root = Toplevel(top2)
    root.geometry('500x500')
    root.title("Registration Form")

    def insert():


        sql = "INSERT INTO kid(name,email,Password,Gender,Country) VALUES(%s,%s,%s,%s,%s)"
        val = (Fullname.get(), Email.get(), password.get(), var.get(), c.get())
        mycs.execute(sql, val)
        mydb.commit()
        print(mycs.rowcount, "inserted successfully")
        root.destroy()
        signin()

    Fullname = StringVar()
    Email = StringVar()
    var = IntVar()
    c = StringVar()
    var1 = IntVar()
    password = StringVar()

    label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root, textvar=Fullname, bd=5)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Email", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root, textvar=Email, bd=5)
    entry_2.place(x=240, y=180)
    label_2 = Label(root, text="password", width=20, font=("bold", 10))
    label_2.place(x=68, y=230)

    entry_2 = Entry(root, textvar=password, bd=5)
    entry_2.place(x=240, y=230)

    label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
    label_3.place(x=70, y=280)

    Radiobutton(root, text="Male", padx=5, variable=var, value="1").place(x=235, y=280)
    Radiobutton(root, text="Female", padx=20, variable=var, value="2").place(x=290, y=280)

    label_4 = Label(root, text="country", width=20, font=("bold", 10))
    label_4.place(x=70, y=330)

    list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];

    droplist = OptionMenu(root, c, *list1)
    droplist.config(width=15)
    c.set('select your country')
    droplist.place(x=240, y=330)

    Button(root, text='Submit', width=20, bg='brown', fg='white', command=insert).place(x=180, y=380)

    root.mainloop()


def game():
    global top
    top = Toplevel(top2)
    top.configure(bg='lightblue')
    top.title("learning Game")
    word_list = ["MANGO", "APPLE", "BANANA", "LITCHI", "GRAPES", "WATERMELON", "POMEGRANATE", "GUAVA", "PINEAPPLE",
                 "KIWI", "ORANGE",
                 "STRAWBERRY", "PLUM", "LEMON", "CHERRY", "COCONUT", "BLUEBERRY", "JACKFRUIT"]

    def newgame():
        global the_word_withSpaces
        global numberofguesses
        numberofguesses = 0
        the_word = random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(" ".join("_" * len(the_word)))

    def guess(letter):
        global numberofguesses
        numberofguesses += 1
        lblNoGuess["text"] = "Number of Guesses:" + str(numberofguesses)
        if numberofguesses < 11:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get() == the_word_withSpaces:
                        messagebox.showinfo("learning Game", "You are Genious")
            else:
                numberofguesses += 1
                if numberofguesses == 11:
                    messagebox.showwarning("learning Game", "Oops,Game Over!!")

    lblWord = StringVar()

    l1 = Label(top, text="Hey,Let's guess the name of a fruit.", bg="lightblue", fg="darkblue", font="bold")
    l1.place(x=10, y=10)
    lblNoGuess = Label(top, text="Number of Guess:0")
    lblNoGuess.place(x=460, y=10)
    Label(top, textvariable=lblWord, font=("consolas 24 bold")).grid(row=0, column=0, columnspan=6, padx=40, pady=60)
    n = 0
    for c in ascii_uppercase:
        Button(top, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1 + n // 9,
                                                                                               column=n % 9)
        n += 1
    Button(top, text="Exit", command=top.quit,font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")
    newgame()
    top.mainloop()



home()