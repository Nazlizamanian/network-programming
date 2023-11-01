#Lab 11 Nazli Zamanian Gustavsson
import sqlite3

data_file = 'score2.txt'

persons_data = []
scores_data = []

with open(data_file, 'r') as file:
    for line in file:
        # Assuming format: identity, first name, last name, points
        identity, first_name, last_name, points = line.strip().split(',')
        persons_data.append((identity, first_name, last_name))
        scores_data.append((points,))

# Step 2: Create an SQLite database and define tables
db_file = 'lab11Database.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create "persons" table with first name and last name
cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
                  identity TEXT PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT)''')

# Create "scores" table with points
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                  points INTEGER)''')


cursor.executemany("INSERT INTO persons VALUES (?, ?, ?)", persons_data)
cursor.executemany("INSERT INTO scores VALUES (?)", scores_data)


# (a) List the 10 persons with the highest total points
cursor.execute('''
    SELECT p.first_name, p.last_name, SUM(s.points) as total_points
    FROM persons p
    JOIN scores s ON p.identity = s.identity
    GROUP BY p.identity
    ORDER BY total_points DESC
    LIMIT 10
''')

highest_total_points = cursor.fetchall()
print("(a) List of 10 persons with the highest total points:")
for row in highest_total_points:
    print(row)

# (b) List the 10 most difficult tasks (minimal total points)
cursor.execute('''
    SELECT s.points
    FROM scores s
    ORDER BY s.points
    LIMIT 10
''')

most_difficult_tasks = cursor.fetchall()
print("\n(b) List of 10 most difficult tasks (minimal total points):")
for row in most_difficult_tasks:
    print(row)

conn.commit()
conn.close()
