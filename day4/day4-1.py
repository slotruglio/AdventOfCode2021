def column(matrix, i):
    return [row[i] for row in matrix]

def boardChecker(board):
    for row in board:
        trueCounter = 0
        for x in row:
            if x[1] == True:
                trueCounter += 1
        if trueCounter == 5:
            return True
    for i in range(0, len(board)):
        trueCounter = 0
        for x in column(board, i):
            if x[1] == True:
                trueCounter += 1
        if trueCounter == 5:
            return True
    return False

with open("input.txt", "r") as f:
    numbers = [int(e) for e in f.readline().split(',')]

    lines = f.readlines()

    boards = []
    curr_board = []

    # create boards with numbers as False
    for line in lines:
        if line != "\n":
            line = line.strip()
            row = line.split(" ")
            tmp = []
            for n in row:
                try:
                    x = int(n)
                    tmp.append([x, False])
                except: count = 0
            curr_board.append(tmp)
            if len(curr_board) == 5:
                boards.append(curr_board)
                curr_board = [] 

    curr_extracted = -1
    counter = 0
    winning_board = []

    for extracted in numbers:
        curr_extracted = extracted
        for board in boards:
            for row in board:
                for x in row:
                    if x[0] == extracted:
                        x[1] = True
        counter += 1
        # bingo check
        if counter > 4:
            for board in boards:
                if boardChecker(board):
                    winning_board = board
                    break
            else: continue
            break
        else: continue

    sum = 0

    print("Winning board is Board [", boards.index(winning_board), "]")
    for row in winning_board:
        for x in row:
            if x[1] == False:
                sum += x[0]
    print("Final score is {}*{} = {}".format(sum, curr_extracted, sum*curr_extracted))


        