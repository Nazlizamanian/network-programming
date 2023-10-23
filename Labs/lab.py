# Lab 2 Nazli Zamanian Gustavsson
pointsPerPerson = {}  

with open("score2.txt", 'r') as file:
    for line in file:
        fields = line.strip().split()

        if len(fields) >= 4:  
            name = " ".join(fields[2:-1])
            points = int(points_str)  

            if name in pointsPerPerson:
                pointsPerPerson[name] += points
            else:
                pointsPerPerson[name] = points

for name, totalPoints in pointsPerPerson.items():
    print(f"{name}: {totalPoints} points")
