import sqlite3

conn = sqlite3.connect('monitor.db')
cursor = conn.cursor()

# Create a table to store every "ping" we do to the API
cursor.execute('''
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        status_code INTEGER,
        latency REAL,
        success INTEGER -- 1 for True, 0 for False
    )
''')
conn.commit()
conn.close()
