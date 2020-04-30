new = ""
total = 0
n = int(input())

for x in range(0,n):
    new = input()
    if new == "Tetrahedron":
        total += 4
    elif new == "Cube":
        total += 6
    elif new == "Octahedron":
        total += 8
    elif new == "Dodecahedron":
        total += 12
    else:
        total += 20

print(total)
