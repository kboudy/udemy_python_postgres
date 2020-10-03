import sqlite3
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # will return dictionary instead of Tuple

def create_table():
    with connection:
        connection.execute(
            "IF NOT EXISTS CREATE TABLE entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?,?);",
                           (entry_content, entry_date))


def get_entries():
    cursor = connection.execute("SELECT * from entries;")
    return cursor