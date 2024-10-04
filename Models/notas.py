import mysql.connector

class NotasCRUD:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        self.cursor = self.db.cursor()

    def create_nota(self, id_disc_fk, id_aluno_fk, nota_final, faltas):
        query = "INSERT INTO Notas (ID_DISC_FK, ID_ALUNO_FK, NOTA_FINAL, FALTAS) VALUES (%s, %s, %s, %s)"
        values = (id_disc_fk, id_aluno_fk, nota_final, faltas)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Nota created successfully.")

    def read_notas(self):
        query = "SELECT * FROM Notas"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for row in records:
            print(row)

    def update_nota(self, id_nota, id_disc_fk, id_aluno_fk, nota_final, faltas):
        query = "UPDATE Notas SET ID_DISC_FK = %s, ID_ALUNO_FK = %s, NOTA_FINAL = %s, FALTAS = %s WHERE ID_NOTA = %s"
        values = (id_disc_fk, id_aluno_fk, nota_final, faltas, id_nota)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Nota updated successfully.")

    def delete_nota(self, id_nota):
        query = "DELETE FROM Notas WHERE ID_NOTA = %s"
        values = (id_nota,)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Nota deleted successfully.")

    def close_connection(self):
        self.cursor.close()
        self.db.close()