import tkinter as tk
from tkinter import *
from tkinter import ttk
import cgi

root = Tk()
root.geometry("1000x600")
root.resizable(False, False)
root.title("Prenotazioni Unito")


def tab():
    def Calendario_Ripetizioni():
        cv1 = Canvas(root, width=1400, height=500)
        cv1.place(x=1, y=1)
        lb1 = Label(root, text="Calendario_Ripetizioni")
        lb1.place(x=450, y=100)
        tab()

    def insegnamenti():
        cv2 = Canvas(root, width=1400, height=1000)
        cv2.place(x=1, y=1)
        lb2 = Label(root, text="insegnamenti")
        lb2.place(x=450, y=100)
        tab()

    def Login():
        # def submit(acc, pw):

        cv3 = Canvas(root, width=1400, height=1000)
        cv3.place(x=1, y=1)
        Label(root, text="Accedi", font="times 15 bold").place(x=160, y=150)
        Account = Label(root, text="Account")
        Account.place(x=100, y=200)
        Password = Label(root, text="Password")
        Password.place(x=100, y=250)
        acc_val = StringVar
        pw_val = StringVar
        acc_entry = Entry(root, textvariable=acc_val)
        acc_entry.place(x=160, y=200)
        pw_entry = Entry(root, textvariable=pw_val)
        pw_entry.place(x=160, y=250)
        submit = Button(root, text="Login")
        tab()

    tab1 = Button(root, text="Calendario Ripetizioni", command=Calendario_Ripetizioni)
    tab1.place(x=5, y=1)
    tab2 = Button(root, text="Lista insegnamenti", command=insegnamenti)
    tab2.place(x=147, y=1)
    tab3 = Button(root, text="Login", command=Login)
    tab3.place(x=270, y=1)


if __name__ == "__main__":
    tab()
    root.mainloop()
