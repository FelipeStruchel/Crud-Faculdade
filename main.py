import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Sistema CRUD")

        self.treeview = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Fone"), show='headings')
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Fone", text="Fone")
        self.treeview.pack()


    def load_data(self):
        records = self.db.read_professores()
        for rec in records:
            self.treeview.insert('', 'end', values=rec)

if __name__ == "__main__":
    db = Database()
    root = tk.Tk()
    app = App(root, db)
    app.load_data()
    root.mainloop()
    db.close_connection()