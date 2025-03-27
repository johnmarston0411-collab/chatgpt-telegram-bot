import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def add_concert(concert: str) -> str:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS concerts (id SERIAL PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO concerts (name) VALUES (%s)", (concert,))
    conn.commit()
    cur.close()
    conn.close()
    return "Концерт добавлен!"

def list_concerts() -> str:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM concerts ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        return "Список концертов пуст."
    return "Список концертов:\n" + "\n".join(f"{i + 1}. {r[0]}" for i, r in enumerate(rows))

def clear_concerts() -> str:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS concerts")
    conn.commit()
    cur.close()
    conn.close()
    return "Список концертов очищен."
