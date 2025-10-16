grid = []
for i in range(7):
    row = []
    for j in range(7):
        if i + j < 7:
            row.append(i + j + 1)
        else:
            row.append(0)  
    grid.append(row)

for row in grid:
    print(row)