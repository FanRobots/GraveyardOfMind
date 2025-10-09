import sqlite3

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
        self._connection = sqlite3.connect("graveyards.db")
        self._cursor = self._connection.cursor()
        self.create_tables_names_tables()

    def create_tables_names_tables(self):
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS names_tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_in_system TEXT NOT NULL)
        """)
        self._connection.commit()

    def create_table_graveyards(self, table, name_table):
        self._cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            content TEXT NOT NULL )
        """)
        self._cursor.execute("INSERT INTO names_tables(name, name_in_system) VALUES (?,?)",(name_table, table))
        self._connection.commit()

    def add_new_gravestone_in_table(self, table, name_gravestone, content):
        self._cursor.execute(f"INSERT INTO {table}(name, content) VALUES (?,?)",(name_gravestone, content))
        self._connection.commit()

    def get_name_table(self, table, row_id):
        self._cursor.execute(f"SELECT name, name_in_system FROM {table} WHERE id=(?)", row_id)
        return self._cursor.fetchone()

    def get_row_from_table(self, table, row_id):
        self._cursor.execute(f"SELECT id, name, content FROM {table} WHERE id=(?)", row_id)
        return self._cursor.fetchone()

    def close(self):
        self._connection.close()


class GraveyardOfMind(App):
    def __init__(self, **kwargs):
        self.data_base = DataBase()
        super().__init__(**kwargs)

    def build(self):
        Window.size = (365, 650)
        return Builder.load_file("screens.kv")

if __name__ == '__main__':
    app = GraveyardOfMind()
    app.run()
    app.data_base.close()
