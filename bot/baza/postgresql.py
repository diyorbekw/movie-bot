import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        self.connection.set_session(autocommit=True)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if parameters is None:
            parameters = ()
        cursor = self.connection.cursor()
        logger(cursor.mogrify(sql, parameters).decode())

        data = None
        try:
            cursor.execute(sql, parameters)
            if commit:
                self.connection.commit()
            if fetchall:
                data = cursor.fetchall()
            if fetchone:
                data = cursor.fetchone()
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            self.connection.rollback()
        finally:
            cursor.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{key} = %s" for key in parameters])
        return sql, tuple(parameters.values())

    def add_user(self, telegram_id: int, full_name: str, phone_number: str):
        sql = """
        INSERT INTO core_user (telegram_id, full_name, phone_number) 
        VALUES (%s, %s, %s);
        """
        self.execute(sql, parameters=(telegram_id, full_name, phone_number), commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM core_user;"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM core_user WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM core_user;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM core_user WHERE TRUE;", commit=True)

    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM core_user;", fetchall=True)

    def get_movie_by_id(self, movie_id):
        sql = "SELECT * FROM core_movie WHERE id = %s;"
        return self.execute(sql, parameters=(movie_id,), fetchone=True)
    