# Experiment 2

import requests
import pandas as pd

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
response = requests.get(url)
issues = response.json()

df_issues = pd.DataFrame(issues)
print(df_issues[['id', 'title', 'state', 'created_at']].head())

import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)''')

# Insert data
cursor.execute("INSERT INTO students VALUES (1, 'John')")
conn.commit()

# Read data
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)

# Update and Delete
cursor.execute("UPDATE students SET name = 'Alice' WHERE id = 1")
cursor.execute("DELETE FROM students WHERE id = 1")
conn.commit()
conn.close()
