import mysql.connector

class AlunosCRUD:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        self.cursor = self.db.cursor()

    def create_aluno(self, nome, email, fone):
        query = "INSERT INTO Alunos (NOME, EMAIL, FONE) VALUES (%s, %s, %s)"
        values = (nome, email, fone)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Aluno created successfully.")

    def read_alunos(self):
        query = "SELECT * FROM Alunos"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for row in records:
            print(row)

    def update_aluno(self, id_aluno, nome, email, fone):
        query = "UPDATE Alunos SET NOME = %s, EMAIL = %s, FONE = %s WHERE ID_ALUNO = %s"
        values = (nome, email, fone, id_aluno)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Aluno updated successfully.")

    def delete_aluno(self, id_aluno):
        query = "DELETE FROM Alunos WHERE ID_ALUNO = %s"
        values = (id_aluno,)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Aluno deleted successfully.")

    def close_connection(self):
        self.cursor.close()
        self.db.close()