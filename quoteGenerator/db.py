import sqlite3
from datetime import datetime, timezone

DB_PATH = "quotes.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, content TEXT, created_at TEXT)")
    conn.commit()
    conn.close()

def save_quote(content: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO quotes (content, created_at) VALUES (?, ?)", (content, datetime.now(timezone.utc).isoformat()))
    conn.commit()
    conn.close()

def get_recent_quotes():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT content, created_at FROM quotes ORDER BY id DESC LIMIT 10")
    quotes = c.fetchall()
    conn.close()
    return [{"quote": q[0], "timestamp": q[1]} for q in quotes]
