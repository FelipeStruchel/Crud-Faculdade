import mysql.connector

class DisciplinasCRUD:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            database='faculdade',
            user='root',
            password='123mudar'
        )
        self.cursor = self.db.cursor()

    def create_disciplina(self, disciplina, carga_horaria, id_prof_fk):
        query = "INSERT INTO Disciplinas (DISCIPLINA, CARGA_HORARIA, ID_PROF_FK) VALUES (%s, %s, %s)"
        values = (disciplina, carga_horaria, id_prof_fk)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Disciplina created successfully.")

    def read_disciplina(self, id_disci):
        query = "SELECT * FROM Disciplinas WHERE ID_DISCI = %s"
        self.cursor.execute(query, (id_disci,))
        return self.cursor.fetchone()
        

    def update_disciplina(self, id_disci, disciplina, carga_horaria, id_prof_fk):
        query = "UPDATE Disciplinas SET DISCIPLINA = %s, CARGA_HORARIA = %s, ID_PROF_FK = %s WHERE ID_DISCI = %s"
        values = (disciplina, carga_horaria, id_prof_fk, id_disci)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Disciplina updated successfully.")

    def delete_disciplina(self, id_disci):
        query = "DELETE FROM Disciplinas WHERE ID_DISCI = %s"
        values = (id_disci,)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Disciplina deleted successfully.")

    def close_connection(self):
        self.cursor.close()
        self.db.close()