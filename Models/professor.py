import mysql.connector
from mysql.connector import Error

class ProfessorCRUD:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='faculdade',
                user='root',
                password='123mudar'
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def create_professor(self, nome, email, fone):
        cursor = self.connection.cursor()
        query = "INSERT INTO Professores (NOME, EMAIL, FONE) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, email, fone))
        self.connection.commit()

    def read_professor(self, id_prof):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Professores where id_prof=%s", (id_prof,))
        return cursor.fetchone()

    def update_professor(self, id_prof, nome, email, fone):
        cursor = self.connection.cursor()
        query = "UPDATE Professores SET NOME=%s, EMAIL=%s, FONE=%s WHERE ID_PROF=%s"
        cursor.execute(query, (nome, email, fone, id_prof))
        self.connection.commit()

    def delete_professor(self, id_prof):
        cursor = self.connection.cursor()
        query = "DELETE FROM Professores WHERE ID_PROF=%s"
        cursor.execute(query, (id_prof,))
        self.connection.commit()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")