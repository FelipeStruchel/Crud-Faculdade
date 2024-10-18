import mysql.connector

class AlunosCRUD:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123mudar",
            database="faculdade"
        )
        self.cursor = self.db.cursor()

    def create_aluno(self, nome, email, fone):
        query = "INSERT INTO Alunos (NOME, EMAIL, FONE) VALUES (%s, %s, %s)"
        values = (nome, email, fone)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Aluno created successfully.")

    def read_aluno(self, id_aluno):
        query = "SELECT * FROM Alunos WHERE ID_ALUNO = %s"
        self.cursor.execute(query, (id_aluno,))
        return self.cursor.fetchone()

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