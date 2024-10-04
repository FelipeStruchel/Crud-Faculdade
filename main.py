import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import matplotlib.pyplot as plt

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema CRUD")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        self.cursor = self.db.cursor()

        self.treeview = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Fone"), show='headings')
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Fone", text="Fone")
        self.treeview.pack()

        self.id_aluno_entry = tk.Entry(root)
        self.id_aluno_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_aluno)
        self.search_button.pack()

        self.graph_button = tk.Button(root, text="Show Average Grades", command=self.show_average_grades)
        self.graph_button.pack()

    def search_aluno(self):
        id_aluno = self.id_aluno_entry.get()
        query = """
        SELECT d.DISCIPLINA, p.NOME, n.NOTA_FINAL, n.FALTAS 
        FROM NOTAS n
        JOIN DISCIPLINAS d ON n.ID_DISC_FK = d.ID_DISCI
        JOIN PROFESSORES p ON d.ID_PROF_FK = p.ID_PROF
        WHERE n.ID_ALUNO_FK = %s
        """
        self.cursor.execute(query, (id_aluno,))
        records = self.cursor.fetchall()
        for row in records:
            self.treeview.insert("", "end", values=row)

    def show_average_grades(self):
        query = """
        SELECT d.DISCIPLINA, AVG(n.NOTA_FINAL) 
        FROM NOTAS n
        JOIN DISCIPLINAS d ON n.ID_DISC_FK = d.ID_DISCI
        GROUP BY d.DISCIPLINA
        """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        disciplines = [row[0] for row in records]
        averages = [row[1] for row in records]

        plt.bar(disciplines, averages)
        plt.xlabel('Disciplinas')
        plt.ylabel('Média das Notas')
        plt.title('Média das Notas por Disciplina')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()