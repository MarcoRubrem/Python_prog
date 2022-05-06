from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1200x600")
root.resizable(False, False)
root.title("Prenotazioni Unito")

utente = "Py_user"


def tab():
    def Ripetizioni():
        cv1 = Canvas(root, width=1400, height=1000)
        cv1.place(x=1, y=150)
        tv = ttk.Treeview(cv1, columns=("Nome Docente", "Cognome Docente", "Corso", "Giorno", "Ora"))
        tv['show'] = "headings"
        tv["columns"] = (1, 2, 3, 4, 5, 6)
        tv.heading(1, text="Nome Docente")
        tv.heading(2, text="Cognome Docente")
        tv.heading(3, text="Corso")
        tv.heading(4, text="Giorno")
        tv.heading(5, text="Ora")
        tv.heading(6, text="Prenota")
        tv['show'] = 'headings'

        def Display():
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb",
                                           database="dbprog")
            cursor = conn.cursor()
            query_sel = "select nome, cognome, corso, giorno, ora from ripetizione where stato like 'libero' order by ora"
            cursor.execute(query_sel)
            records = cursor.fetchall()
            if len(records) != 0:
                tv.delete(*tv.get_children())
                for i in records:
                    tv.insert('', END, values=i)
            cursor.close()
            conn.close()

        def prenota():
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb",
                                           database="dbprog")
            cursor = conn.cursor()
            info = tv.focus()
            data = tv.item(info)
            row = data['values']
            if len(row) == 0:
                messagebox.showerror("showerror", "Attenzione! Selezionare una ripetizione da prenotare!")
            else:
                update_query = "update ripetizione set stato='occupato' where nome like %s and cognome like %s and corso like %s and giorno like %s and ora like %s"
                insert_query = "insert into prenotazione (`utente`, `nome_docente`, `cognome_docente`, `corso`, `giorno`, `ora`, `stato`) values(%s, %s, %s, %s, %s, %s, 'attiva')"
                rip = (row[0], row[1], row[2], row[3], row[4])
                booking = (utente, row[0], row[1], row[2], row[3], row[4])
                cursor.execute(update_query, rip)
                cursor.execute(insert_query, booking)
                conn.commit()
                messagebox.showinfo("showinfo", "Prenotazione effettuata con successo")
                Display()

        Display()
        tv.pack()
        Booking = Button(cv1, text="Prenota", command=prenota, bg='green',
                         fg='white', relief='flat', width=30, height=13)
        Booking.place(x=1000, y=27)
        tab()

    def Prenotazioni():
        cv3 = Canvas(root, width=1400, height=1000)
        cv3.place(x=1, y=150)

        tv_book = ttk.Treeview(cv3, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="10")
        tv_book.heading(1, text="Nome Docente")
        tv_book.heading(2, text="Cognome Docente")
        tv_book.heading(3, text="Corso")
        tv_book.heading(4, text="Giorno")
        tv_book.heading(5, text="Ora")
        tv_book.heading(6, text="Stato")
        tv_book.heading(7, text="Azione")
        tv_book.column(1, width=120)
        tv_book.column(2, width=120)
        tv_book.column(6, width=155)

        def Display():
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb",
                                           database="dbprog")
            cursor = conn.cursor()
            query_sel = "select nome_docente, cognome_docente, corso, giorno, ora, stato from prenotazione where utente like 'Py_user' order by stato, ora"
            cursor.execute(query_sel)
            records = cursor.fetchall()
            if len(records) != 0:
                tv_book.delete(*tv_book.get_children())
                for i in records:
                    tv_book.insert('', END, values=i)
            cursor.close()
            conn.close()

        def Booking_done():
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb",
                                           database="dbprog")
            cursor = conn.cursor()
            info = tv_book.focus()
            data = tv_book.item(info)
            row = data['values']
            if len(row) == 0:
                messagebox.showerror("showerror", "Attenzione! Selezionare una riga per prenotare")
            elif row[5] != 'attiva':
                messagebox.showwarning("showwarning", "Selezionare una ripetizione attiva")
            else:
                update_query = "update ripetizione set stato='libero' where nome like %s and cognome like %s and corso like %s and giorno like %s and ora like %s"
                insert_query = "update prenotazione set stato='effettuata' where utente like %s and nome_docente like %s and cognome_docente like %s and corso like %s and giorno like %s and ora like %s"
                rip = (row[0], row[1], row[2], row[3], row[4])
                booking = (utente, row[0], row[1], row[2], row[3], row[4])
                cursor.execute(update_query, rip)
                cursor.execute(insert_query, booking)
                conn.commit()
                messagebox.showinfo("showinfo", "Prenotazione effettuata con successo")
                Display()

        def cancel_Booking():
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb",
                                           database="dbprog")
            cursor = conn.cursor()
            info = tv_book.focus()
            data = tv_book.item(info)
            row = data['values']
            if len(row) == 0:
                messagebox.showerror("showerror", "Attenzione! Selezionare una ripetizione attiva!")
            elif row[5] != 'attiva':
                messagebox.showwarning("showwarning", "Selezionare una ripetizione attiva")
            else:
                update_query = "update ripetizione set stato='libero' where nome like %s and cognome like %s and corso like %s and giorno like %s and ora like %s"
                insert_query = "update prenotazione set stato='cancellata' where utente like %s and nome_docente like %s and cognome_docente like %s and corso like %s and giorno like %s and ora like %s "
                rip = (row[0], row[1], row[2], row[3], row[4])
                booking = (utente, row[0], row[1], row[2], row[3], row[4])
                cursor.execute(update_query, rip)
                cursor.execute(insert_query, booking)
                conn.commit()
                messagebox.showinfo("showinfo", "Prenotazione cancellata con successo")
                Display()

        Display()
        tv_book.pack()
        Set_Booking_done = Button(cv3, text="Effettua Prenotazione", bg='green',
                                  fg='white', relief='flat', width=28, height=6, command=Booking_done)
        Set_Booking_done.place(x=997, y=25)
        cancel_Booking = Button(cv3, text="Cancella Prenotazione", bg='red',
                                fg='white', relief='flat', width=28, height=7, command=cancel_Booking)
        cancel_Booking.place(x=997, y=120)
        tab()

    tab1 = Button(root, text="RIPETIZIONI DISPONIBILI", command=Ripetizioni, bg='grey',
                  fg='white', relief='flat', width=27, height=4)
    myFont = font.Font(weight="bold", family='sans serif', size=9)
    tab1['font'] = myFont
    tab1.place(x=400, y=80)
    tab2 = Button(root, text="LE TUE PRENOTAZIONI", command=Prenotazioni, relief='flat', bg='red',
                  fg='white', width=28, height=4)
    tab2['font'] = myFont
    tab2.place(x=600, y=80)


if __name__ == "__main__":
    tab()
    root.mainloop()
