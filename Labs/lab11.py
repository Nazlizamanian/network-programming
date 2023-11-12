#Lab 11 Nazli Zamanian Gustavsson
import sqlite3

conn = sqlite3.connect('score_data.db')
cursor = conn.cursor() 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        task_number INTEGER,
        points INTEGER,
        person_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES persons(id)
    )
''')

# Read data from the file and insert it into the tables
with open('score2.txt', 'r') as file:
    for line in file:
        parts = line.split()
        task_number = int(parts[1])
        first_name = parts[2]
        last_name = parts[3]
        points = int(parts[4])
        
        cursor.execute('INSERT INTO persons (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        
        cursor.execute('SELECT id FROM persons WHERE first_name=? AND last_name=?', (first_name, last_name))
        person_id = cursor.fetchone()[0] #use to our ID to our scores table. 
        
        cursor.execute('INSERT INTO scores (task_number, points, person_id) VALUES (?, ?, ?)', (task_number, points, person_id))
        
#(a) List the 10 persons with the highest total points
cursor.execute('''
    SELECT p.first_name, p.last_name, SUM(s.points) AS total_points
    FROM persons p
    JOIN scores s ON p.id = s.person_id
    GROUP BY p.id
    ORDER BY total_points DESC
    LIMIT 10
''')
top_10_persons = cursor.fetchall()

# (b) List the 10 most difficult tasks (minimal total points)
cursor.execute('''
    SELECT task_number, SUM(points) AS total_points
    FROM scores
    GROUP BY task_number
    ORDER BY total_points
    LIMIT 10
''')
most_difficult_tasks = cursor.fetchall()


def print_create_table_person():
    print("Tables\n")
    print("Persons table\n")
    cursor.execute("SELECT * FROM persons")
    persons_table = cursor.fetchall()
    for row in persons_table:
        print(row)
        
def print_create_table_scores():
    print("Tables\n")
    print("Scores table\n")
    cursor.execute("SELECT * FROM scores")
    scores_table = cursor.fetchall()
    for row in scores_table:
        print(row)
        
        
def print_sql_results():
    print("(a) List of the 10 persons with the highest total points: ")
    for person in top_10_persons:
        print(f"{person[0]} {person[1]} - Total Points: {person[2]}")

    print("\n(b) List of the 10 most difficult tasks: ")
    for task in most_difficult_tasks:
        print(f"Task {task[0]} - Total Points: {task[1]}")  
    
    
while True:
    choice = input("\n Enter 1 to print table Person, 2 to print table Scores or 3 to print SQL query results\n")
    
    if choice == '1':
        print("Printing creating tables persons\n")
        print_create_table_person()
    if choice == '2':
        print("Printing creating tables scores\n")
        print_create_table_scores()
    if choice == '3': 
        print("Printing SQL query results\n")
        print_sql_results()
