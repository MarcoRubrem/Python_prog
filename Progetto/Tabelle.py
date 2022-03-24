import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry("1000x600")
root.resizable(False, False)
root.title("Prenotazioni Unito")

frm = Frame(root)
frm.pack(side=tk.LEFT)
tv = ttk.Treeview(frm, columns=("Nome Docente", "Cognome Docente", "Corso", "Giorno", "Ora"))
tv['show'] = "headings";

tv["columns"] = ("Nome Docente", "Cognome Docente", "Corso", "Giorno", "Ora")

tv.heading("Nome Docente", text="Nome Docente")
tv.heading("Cognome Docente", text="Cognome Docente")
tv.heading("Corso", text="Corso")
tv.heading("Giorno", text="Giorno")
tv.heading("Ora", text="Ora")
tv['show'] = 'headings'


def Display():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb", database="dbprog")
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
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="tweb", database="dbprog")
    cursor = conn.cursor()
    info = tv.focus()
    data = tv.item(info)
    row = data['values']
    if len(row) == 0:
        print("Selezionare una riga per prenotare")
    else:
        update_query = "update ripetizione set stato='occupato' where nome like %s and cognome like %s and corso like %s and giorno like %s and ora like %s"
        insert_query = "insert into prenotazione (`utente`, `nome_docente`, `cognome_docente`, `corso`, `giorno`, `ora`, `stato`) values(%s, %s, %s, %s, %s, %s, 'attiva')"
        rip = (row[0], row[1], row[2], row[3], row[4])
        booking = (utente, row[0], row[1], row[2], row[3], row[4])
        cursor.execute(update_query, rip)
        cursor.execute(insert_query, booking)
        conn.commit()
        Display()


Display()
tv.pack()

deletebutton = Button(root, text="prenota", command=prenota)
deletebutton.place(x=300, y=500)

if __name__ == "__main__":
    root.mainloop()
