import sqlite3
from pathlib import Path

Base_dir = Path(__file__).resolve().parent.parent

DB_PATH = Base_dir/"SGAE.db"

def createConnection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection