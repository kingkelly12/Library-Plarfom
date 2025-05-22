# CRUD OPERATIONS

from db import get_connection
from models.category import Category


class CategoryResource:

    @staticmethod
    def create(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO categories (title, description)
                VALUES (%s, %s)
                RETURNING id 
            """,
            (self.title, self.description)
            )
            print(f"{self.title} has been added successfully!!")
        return True

    @staticmethod
    def list(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM categories
            """)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        return rows

    @staticmethod
    def update(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                UPDATE categories
                SET title = %s, description = %s
                WHERE id = %s
            """,
            (self.title, self.description, self.id)
            )
            print(f"{self.title} has been updated successfully!!")
        return True

    @staticmethod
    def delete(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                DELETE FROM categories
                WHERE id = %s
            """,
            (self.id,)
            )
            print(f"{self.title} has been deleted successfully!!")
        return True

    @staticmethod
    def listone(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM categories
                WHERE id = %s
            """,
            (self.id,)
            )
            row = cur.fetchone()
            print(row)
        return row      

