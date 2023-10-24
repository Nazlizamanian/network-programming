# Lab 2 Nazli Zamanian Gustavsson
pointsPerPerson = {}

with open("score2.txt", 'r') as file:
    for line in file:
       
        elements = line.strip().split()
        
        # Ensure each line has the expected format (5 elements)
        if len(elements) == 5 and elements[0] == "upg.":
            name = f"{elements[2]} {elements[3]}"  # Combine first name and last name
            points = int(elements[4])  # Extract points as an integer

            # Update the points for the person in the dictionary
            if name in pointsPerPerson:
                pointsPerPerson[name] += points
            else:
                pointsPerPerson[name] = points


max_points = max(pointsPerPerson.values())
top_scorers = [name for name, points in pointsPerPerson.items() if points == max_points]

for name in top_scorers:
    print(f"{name} got the most points: {max_points} points.")
