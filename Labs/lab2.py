# Lab 2 Nazli Zamanian Gustavsson
pointsPerPerson = {}

with open("score2.txt", 'r') as file:
    for line in file:
       
        elements = line.strip().split() #Using the split() 
    
        if len(elements) == 5 and elements[0] == "upg.":
            name = f"{elements[2]} {elements[3]}" #String the f & l name.
            points = int(elements[4])  # Extract points as an int.

            if name in pointsPerPerson:
                pointsPerPerson[name] += points
            else:
                pointsPerPerson[name] = points

max_points = max(pointsPerPerson.values())
top_scorers = [name for name, points in pointsPerPerson.items() if points == max_points]

for name in top_scorers:
    print(f"{name} got the most points: {max_points} points.")

# The winner was Maria Johansson with 37 points and 
# Kristina Larsson who got equally the same amount, 37 points. 