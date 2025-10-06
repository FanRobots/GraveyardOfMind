import sqlite3

from docutils.nodes import table
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    pass

class GraveyardsScreen(Screen):
    pass

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("graveyards.db")
        self.cursor = self.connection.cursor()
        self.create_tables_names_tables()

    def create_tables_names_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS names_tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_in_system TEXT NOT NULL)
        """)
        self.connection.commit()

    def create_table_graveyards(self, table, name_table):
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            content TEXT NOT NULL )
        """)
        self.cursor.execute("INSERT INTO names_tables(name, name_in_system) VALUES (?,?)",(name_table, table))
        self.connection.commit()

    def add_new_gravestone_in_table(self, table, name_gravestone, content):
        self.cursor.execute(f"INSERT INTO {table}(name, content) VALUES (?,?)",(name_gravestone, content))
        self.connection.commit()

    def get_name_table(self, table, row_id):
        self.cursor.execute(f"SELECT name, name_in_system FROM {table} WHERE id=(?)", row_id)
        return self.cursor.fetchone()

    def get_row_from_table(self, table, row_id):
        self.cursor.execute(f"SELECT id, name, content FROM {table} WHERE id=(?)", row_id)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()


class GraveyardOfMind(App):
    def build(self):
        Window.size = (365, 650)
        Builder.load_file("style.kv")
        return Builder.load_file("screens.kv")

if __name__ == '__main__':
    GraveyardOfMind().run()
