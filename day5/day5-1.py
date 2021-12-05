with open("dummy.txt", "r") as f:
    lines = [e.strip() for e in f.readlines()]

    matrix = []
    for i in range(0,9):
        row = []
        for j in range(0,9):
            row.append(".")
        matrix.append(row)
    
    for line in lines:
        tmp = line.split("->")
        start = tmp[0]
        end = tmp[1]