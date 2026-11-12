import sqlite3

def initialize_db():
    connection = sqlite3.connect("talentfinder.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS children (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            child_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            talent TEXT NOT NULL,
            parent_name TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_child(child_name, age, gender, talent, parent_name):
    connection = sqlite3.connect("talentfinder.db")

    connection.execute("""
        INSERT INTO children
        (child_name, age, gender, talent, parent_name)
        VALUES (?, ?, ?, ?, ?)
    """, (child_name, age, gender, talent, parent_name))

    connection.commit()
    connection.close()
