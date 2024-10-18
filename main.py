import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import matplotlib.pyplot as plt
from Models.professor import ProfessorCRUD  
from Models.disciplinas import DisciplinasCRUD  
from Models.notas import NotasCRUD
from Models.alunos import AlunosCRUD

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema CRUD")
        
        self.professor_db = ProfessorCRUD() 
        self.disciplina_db = DisciplinasCRUD()
        self.nota_db = NotasCRUD()
        self.aluno_db = AlunosCRUD()
        
        self.db_connection = mysql.connector.connect(
            host='localhost',
            database='faculdade',
            user='root',
            password='123mudar'
        )
        
        self.cursor = self.db_connection.cursor()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.create_professor_tab()
        self.create_disciplina_tab()
        self.create_nota_tab()
        self.create_aluno_tab()
        self.create_consulta_tab()
        self.create_grafico_tab()
        
    def create_professor_tab(self):
        professor_frame = ttk.Frame(self.notebook)
        self.notebook.add(professor_frame, text="Cadastrar Professor")

        ttk.Label(professor_frame, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.professor_id_entry = ttk.Entry(professor_frame)
        self.professor_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(professor_frame, text="Nome:").grid(row=1, column=0, padx=10, pady=10)
        self.professor_nome_entry = ttk.Entry(professor_frame)
        self.professor_nome_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(professor_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.professor_email_entry = ttk.Entry(professor_frame)
        self.professor_email_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(professor_frame, text="Telefone:").grid(row=3, column=0, padx=10, pady=10)
        self.professor_telefone_entry = ttk.Entry(professor_frame)
        self.professor_telefone_entry.grid(row=3, column=1, padx=10, pady=10)

        self.save_professor_button = ttk.Button(professor_frame, text="Salvar", command=self.save_professor)
        self.save_professor_button.grid(row=4, columnspan=2, pady=10)

        self.update_professor_button = ttk.Button(professor_frame, text="Atualizar", command=self.update_professor)
        self.update_professor_button.grid(row=5, columnspan=2, pady=10)

        self.search_professor_button = ttk.Button(professor_frame, text="Pesquisar", command=self.search_professor)
        self.search_professor_button.grid(row=6, columnspan=2, pady=10)

        self.delete_professor_button = ttk.Button(professor_frame, text="Deletar", command=self.delete_professor)
        self.delete_professor_button.grid(row=7, columnspan=2, pady=10)

    def save_professor(self):
        nome = self.professor_nome_entry.get()
        email = self.professor_email_entry.get()
        telefone = self.professor_telefone_entry.get()

        if nome and email and telefone:
            self.professor_db.create_professor(nome, email, telefone)
            messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
            self.professor_nome_entry.delete(0, tk.END)
            self.professor_email_entry.delete(0, tk.END)
            self.professor_telefone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def update_professor(self):
        id_prof = self.professor_id_entry.get()
        nome = self.professor_nome_entry.get()
        email = self.professor_email_entry.get()
        telefone = self.professor_telefone_entry.get()

        if id_prof and nome and email and telefone:
            self.professor_db.update_professor(id_prof, nome, email, telefone)
            messagebox.showinfo("Sucesso", "Professor atualizado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def search_professor(self):
        id_prof = self.professor_id_entry.get()

        if id_prof:
            professor = self.professor_db.read_professor(id_prof)
            if professor:
                self.professor_nome_entry.delete(0, tk.END)
                self.professor_nome_entry.insert(0, professor[1])
                self.professor_email_entry.delete(0, tk.END)
                self.professor_email_entry.insert(0, professor[2])
                self.professor_telefone_entry.delete(0, tk.END)
                self.professor_telefone_entry.insert(0, professor[3])
            else:
                messagebox.showwarning("Atenção", "Professor não encontrado!")
        else:
            messagebox.showwarning("Atenção", "ID do professor é obrigatório!")

    def delete_professor(self):
        id_prof = self.professor_id_entry.get()

        if id_prof:
            try:
                self.professor_db.delete_professor(id_prof)
                messagebox.showinfo("Sucesso", "Professor deletado com sucesso!")
                self.professor_id_entry.delete(0, tk.END)
                self.professor_nome_entry.delete(0, tk.END)
                self.professor_email_entry.delete(0, tk.END)
                self.professor_telefone_entry.delete(0, tk.END)
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showwarning("Erro", f"Não é possível deletar o professor. Ele está vinculado a uma disciplina.")
        else:
            messagebox.showwarning("Atenção", "ID do professor é obrigatório!")

    def create_disciplina_tab(self):
        disciplina_frame = ttk.Frame(self.notebook)
        self.notebook.add(disciplina_frame, text="Cadastrar Disciplina")

        ttk.Label(disciplina_frame, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.disciplina_id_entry = ttk.Entry(disciplina_frame)
        self.disciplina_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(disciplina_frame, text="Disciplina:").grid(row=1, column=0, padx=10, pady=10)
        self.disciplina_nome_entry = ttk.Entry(disciplina_frame)
        self.disciplina_nome_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(disciplina_frame, text="Carga Horária:").grid(row=2, column=0, padx=10, pady=10)
        self.disciplina_carga_horaria_entry = ttk.Entry(disciplina_frame)
        self.disciplina_carga_horaria_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(disciplina_frame, text="Professor ID:").grid(row=3, column=0, padx=10, pady=10)
        self.disciplina_prof_id_entry = ttk.Entry(disciplina_frame)
        self.disciplina_prof_id_entry.grid(row=3, column=1, padx=10, pady=10)

        self.save_disciplina_button = ttk.Button(disciplina_frame, text="Salvar", command=self.save_disciplina)
        self.save_disciplina_button.grid(row=4, columnspan=2, pady=10)

        self.update_disciplina_button = ttk.Button(disciplina_frame, text="Atualizar", command=self.update_disciplina)
        self.update_disciplina_button.grid(row=5, columnspan=2, pady=10)

        self.search_disciplina_button = ttk.Button(disciplina_frame, text="Pesquisar", command=self.search_disciplina)
        self.search_disciplina_button.grid(row=6, columnspan=2, pady=10)

        self.delete_disciplina_button = ttk.Button(disciplina_frame, text="Deletar", command=self.delete_disciplina)
        self.delete_disciplina_button.grid(row=7, columnspan=2, pady=10)

    def save_disciplina(self):
        nome = self.disciplina_nome_entry.get()
        carga_horaria = self.disciplina_carga_horaria_entry.get()
        prof_id = self.disciplina_prof_id_entry.get()

        if nome and carga_horaria and prof_id:
            self.disciplina_db.create_disciplina(nome, carga_horaria, prof_id)
            messagebox.showinfo("Sucesso", "Disciplina cadastrada com sucesso!")
            self.disciplina_nome_entry.delete(0, tk.END)
            self.disciplina_carga_horaria_entry.delete(0, tk.END)
            self.disciplina_prof_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def update_disciplina(self):
        id_disc = self.disciplina_id_entry.get()
        nome = self.disciplina_nome_entry.get()
        carga_horaria = self.disciplina_carga_horaria_entry.get()
        prof_id = self.disciplina_prof_id_entry.get()

        if id_disc and nome and carga_horaria and prof_id:
            self.disciplina_db.update_disciplina(id_disc, nome, carga_horaria, prof_id)
            messagebox.showinfo("Sucesso", "Disciplina atualizada com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def search_disciplina(self):
        id_disc = self.disciplina_id_entry.get()

        if id_disc:
            disciplina = self.disciplina_db.read_disciplina(id_disc)
            if disciplina:
                self.disciplina_nome_entry.delete(0, tk.END)
                self.disciplina_nome_entry.insert(0, disciplina[1])
                self.disciplina_carga_horaria_entry.delete(0, tk.END)
                self.disciplina_carga_horaria_entry.insert(0, disciplina[2])
                self.disciplina_prof_id_entry.delete(0, tk.END)
                self.disciplina_prof_id_entry.insert(0, disciplina[3])
            else:
                messagebox.showwarning("Atenção", "Disciplina não encontrada!")
        else:
            messagebox.showwarning("Atenção", "ID da disciplina é obrigatório!")

    def delete_disciplina(self):
        id_disc = self.disciplina_id_entry.get()

        if id_disc:
            self.disciplina_db.delete_disciplina(id_disc)
            messagebox.showinfo("Sucesso", "Disciplina deletada com sucesso!")
            self.disciplina_id_entry.delete(0, tk.END)
            self.disciplina_nome_entry.delete(0, tk.END)
            self.disciplina_carga_horaria_entry.delete(0, tk.END)
            self.disciplina_prof_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "ID da disciplina é obrigatório!")

    def create_nota_tab(self):
        nota_frame = ttk.Frame(self.notebook)
        self.notebook.add(nota_frame, text="Cadastrar Nota")

        ttk.Label(nota_frame, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.nota_id_entry = ttk.Entry(nota_frame)
        self.nota_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(nota_frame, text="Disciplina ID:").grid(row=1, column=0, padx=10, pady=10)
        self.nota_disc_id_entry = ttk.Entry(nota_frame)
        self.nota_disc_id_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(nota_frame, text="Aluno ID:").grid(row=2, column=0, padx=10, pady=10)
        self.nota_aluno_id_entry = ttk.Entry(nota_frame)
        self.nota_aluno_id_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(nota_frame, text="Nota Final:").grid(row=3, column=0, padx=10, pady=10)
        self.nota_final_entry = ttk.Entry(nota_frame)
        self.nota_final_entry.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(nota_frame, text="Faltas:").grid(row=4, column=0, padx=10, pady=10)
        self.nota_faltas_entry = ttk.Entry(nota_frame)
        self.nota_faltas_entry.grid(row=4, column=1, padx=10, pady=10)

        self.save_nota_button = ttk.Button(nota_frame, text="Salvar", command=self.save_nota)
        self.save_nota_button.grid(row=5, columnspan=2, pady=10)

        self.update_nota_button = ttk.Button(nota_frame, text="Atualizar", command=self.update_nota)
        self.update_nota_button.grid(row=6, columnspan=2, pady=10)

        self.search_nota_button = ttk.Button(nota_frame, text="Pesquisar", command=self.search_nota)
        self.search_nota_button.grid(row=7, columnspan=2, pady=10)

        self.delete_nota_button = ttk.Button(nota_frame, text="Deletar", command=self.delete_nota)
        self.delete_nota_button.grid(row=8, columnspan=2, pady=10)

    def save_nota(self):
        id_disc = self.nota_disc_id_entry.get()
        id_aluno = self.nota_aluno_id_entry.get()
        nota_final = self.nota_final_entry.get()
        faltas = self.nota_faltas_entry.get()
    
        if id_disc and id_aluno and nota_final and faltas:
            self.nota_db.create_nota(id_disc, id_aluno, nota_final, faltas)
            messagebox.showinfo("Sucesso", "Nota cadastrada com sucesso!")
            self.nota_disc_id_entry.delete(0, tk.END)
            self.nota_aluno_id_entry.delete(0, tk.END)
            self.nota_final_entry.delete(0, tk.END)
            self.nota_faltas_entry.delete(0, tk.END)
    
            self.db_connection.close()
            self.db_connection = mysql.connector.connect(
                host='localhost',
                database='faculdade',
                user='root',
                password='123mudar'
            )
            self.cursor = self.db_connection.cursor()
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def update_nota(self):
        id_nota = self.nota_id_entry.get()
        disc_id = self.nota_disc_id_entry.get()
        aluno_id = self.nota_aluno_id_entry.get()
        nota_final = self.nota_final_entry.get()
        faltas = self.nota_faltas_entry.get()

        if id_nota and disc_id and aluno_id and nota_final and faltas:
            try:
                self.nota_db.update_nota(id_nota, disc_id, aluno_id, nota_final, faltas)
                self.db_connection.close()
                self.db_connection = mysql.connector.connect(
                    host='localhost',
                    database='faculdade',
                    user='root',
                    password='123mudar'
                )
                self.cursor = self.db_connection.cursor()
                messagebox.showinfo("Sucesso", "Nota atualizada com sucesso!")
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showwarning("Erro", "Erro de integridade referencial. Verifique se os IDs de disciplina e aluno existem.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def search_nota(self):
        id_nota = self.nota_id_entry.get()

        if id_nota:
            nota = self.nota_db.read_nota(id_nota)
            if nota:
                self.nota_disc_id_entry.delete(0, tk.END)
                self.nota_disc_id_entry.insert(0, nota[1])
                self.nota_aluno_id_entry.delete(0, tk.END)
                self.nota_aluno_id_entry.insert(0, nota[2])
                self.nota_final_entry.delete(0, tk.END)
                self.nota_final_entry.insert(0, nota[3])
                self.nota_faltas_entry.delete(0, tk.END)
                self.nota_faltas_entry.insert(0, nota[4])
            else:
                messagebox.showwarning("Atenção", "Nota não encontrada!")
        else:
            messagebox.showwarning("Atenção", "ID da nota é obrigatório!")

    def delete_nota(self):
        id_nota = self.nota_id_entry.get()

        if id_nota:
            try:
                self.nota_db.delete_nota(id_nota)
                messagebox.showinfo("Sucesso", "Nota deletada com sucesso!")
                self.nota_id_entry.delete(0, tk.END)
                self.nota_disc_id_entry.delete(0, tk.END)
                self.nota_aluno_id_entry.delete(0, tk.END)
                self.nota_final_entry.delete(0, tk.END)
                self.nota_faltas_entry.delete(0, tk.END)
                self.db_connection.close()
                self.db_connection = mysql.connector.connect(
                    host='localhost',
                    database='faculdade',
                    user='root',
                    password='123mudar'
                )
                self.cursor = self.db_connection.cursor()
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showwarning("Erro", "Não é possível deletar a nota. Ela está vinculada a uma disciplina ou aluno.")
        else:
            messagebox.showwarning("Atenção", "ID da nota é obrigatório!")
    
    def create_aluno_tab(self):
        aluno_frame = ttk.Frame(self.notebook)
        self.notebook.add(aluno_frame, text="Cadastrar Aluno")

        ttk.Label(aluno_frame, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.aluno_id_entry = ttk.Entry(aluno_frame)
        self.aluno_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(aluno_frame, text="Nome:").grid(row=1, column=0, padx=10, pady=10)
        self.aluno_nome_entry = ttk.Entry(aluno_frame)
        self.aluno_nome_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(aluno_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.aluno_email_entry = ttk.Entry(aluno_frame)
        self.aluno_email_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(aluno_frame, text="Telefone:").grid(row=3, column=0, padx=10, pady=10)
        self.aluno_fone_entry = ttk.Entry(aluno_frame)
        self.aluno_fone_entry.grid(row=3, column=1, padx=10, pady=10)

        self.save_aluno_button = ttk.Button(aluno_frame, text="Salvar", command=self.save_aluno)
        self.save_aluno_button.grid(row=4, columnspan=2, pady=10)

        self.update_aluno_button = ttk.Button(aluno_frame, text="Atualizar", command=self.update_aluno)
        self.update_aluno_button.grid(row=5, columnspan=2, pady=10)

        self.search_aluno_button = ttk.Button(aluno_frame, text="Pesquisar", command=self.search_aluno)
        self.search_aluno_button.grid(row=6, columnspan=2, pady=10)

        self.delete_aluno_button = ttk.Button(aluno_frame, text="Deletar", command=self.delete_aluno)
        self.delete_aluno_button.grid(row=7, columnspan=2, pady=10)

    def save_aluno(self):
        nome = self.aluno_nome_entry.get()
        email = self.aluno_email_entry.get()
        fone = self.aluno_fone_entry.get()

        if nome and email and fone:
            self.aluno_db.create_aluno(nome, email, fone)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            self.aluno_nome_entry.delete(0, tk.END)
            self.aluno_email_entry.delete(0, tk.END)
            self.aluno_fone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def update_aluno(self):
        id_aluno = self.aluno_id_entry.get()
        nome = self.aluno_nome_entry.get()
        email = self.aluno_email_entry.get()
        fone = self.aluno_fone_entry.get()

        if id_aluno and nome and email and fone:
            self.aluno_db.update_aluno(id_aluno, nome, email, fone)
            messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def search_aluno(self):
        id_aluno = self.aluno_id_entry.get()

        if id_aluno:
            aluno = self.aluno_db.read_aluno(id_aluno)
            if aluno:
                self.aluno_nome_entry.delete(0, tk.END)
                self.aluno_nome_entry.insert(0, aluno[1])
                self.aluno_email_entry.delete(0, tk.END)
                self.aluno_email_entry.insert(0, aluno[2])
                self.aluno_fone_entry.delete(0, tk.END)
                self.aluno_fone_entry.insert(0, aluno[3])
            else:
                messagebox.showwarning("Atenção", "Aluno não encontrado!")
        else:
            messagebox.showwarning("Atenção", "ID do aluno é obrigatório!")

    def delete_aluno(self):
        id_aluno = self.aluno_id_entry.get()

        if id_aluno:
            try:
                self.aluno_db.delete_aluno(id_aluno)
                messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
                self.aluno_id_entry.delete(0, tk.END)
                self.aluno_nome_entry.delete(0, tk.END)
                self.aluno_email_entry.delete(0, tk.END)
                self.aluno_fone_entry.delete(0, tk.END)
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showwarning("Erro", "Não é possível deletar o aluno. Ele está vinculado a uma nota.")
        else:
            messagebox.showwarning("Atenção", "ID do aluno é obrigatório!")
            
    def create_consulta_tab(self):
        consulta_frame = ttk.Frame(self.notebook)
        self.notebook.add(consulta_frame, text="Consultar Notas")

        ttk.Label(consulta_frame, text="ID do Aluno:").grid(row=0, column=0, padx=10, pady=10)
        self.consulta_aluno_id_entry = ttk.Entry(consulta_frame)
        self.consulta_aluno_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.consulta_button = ttk.Button(consulta_frame, text="Consultar", command=self.consulta_notas)
        self.consulta_button.grid(row=0, column=2, padx=10, pady=10)

        self.treeview = ttk.Treeview(consulta_frame, columns=("Disciplina", "Professor", "Nota Final", "Faltas"), show='headings')
        self.treeview.heading("Disciplina", text="Disciplina")
        self.treeview.heading("Professor", text="Professor")
        self.treeview.heading("Nota Final", text="Nota Final")
        self.treeview.heading("Faltas", text="Faltas")
        self.treeview.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def consulta_notas(self):
        id_aluno = self.consulta_aluno_id_entry.get()

        if id_aluno:
            query = """
            SELECT d.DISCIPLINA, p.NOME, n.NOTA_FINAL, n.FALTAS 
            FROM Notas n
            JOIN Disciplinas d ON n.ID_DISC_FK = d.ID_DISCI
            JOIN Professores p ON d.ID_PROF_FK = p.ID_PROF
            WHERE n.ID_ALUNO_FK = %s
            """
            self.cursor.execute(query, (id_aluno,))
            records = self.cursor.fetchall()

            for row in self.treeview.get_children():
                self.treeview.delete(row)

            for record in records:
                self.treeview.insert("", tk.END, values=record)
        else:
            messagebox.showwarning("Atenção", "ID do aluno é obrigatório!")
            
            
    def create_grafico_tab(self):
        grafico_frame = ttk.Frame(self.notebook)
        self.notebook.add(grafico_frame, text="Gráfico de Médias")

        self.grafico_button = ttk.Button(grafico_frame, text="Gerar Gráfico", command=self.gerar_grafico)
        self.grafico_button.pack(pady=20)

    def gerar_grafico(self):
        query = """
        SELECT d.DISCIPLINA, AVG(n.NOTA_FINAL) as MEDIA_NOTAS
        FROM Notas n
        JOIN Disciplinas d ON n.ID_DISC_FK = d.ID_DISCI
        GROUP BY d.DISCIPLINA
        """
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        disciplinas = [record[0] for record in records]
        medias = [record[1] for record in records]

        plt.figure(figsize=(10, 6))
        plt.bar(disciplinas, medias, color='blue')
        plt.xlabel('Disciplinas')
        plt.ylabel('Média das Notas')
        plt.title('Média das Notas dos Alunos por Disciplina')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
            

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()