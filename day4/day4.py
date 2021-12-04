lines = [i.replace("\n", "") for i in open("4.txt", "r")]

nums = lines.pop(0).split(",") # get the numbers
lines.pop(0) # remove the empty line

boards = [] # init boards

sboard = [] # init current board
for i in range(len(lines)):
    sboard.append([[0, int(lines[i][j:j+2])] for j in range(0, len(lines[i]), 3)]) if len(lines[i]) != 0 else None
    if i == len(lines) - 1 or len(lines[i]) == 0:
        boards.append(sboard)
        sboard = []

#print(boards)

def checkWon(j):
    return True if sum([a[0] for a in j]) == len(j) - 1 else False

def searchBingo():
    winners = []
    won = []
    for num in nums:
        for i in range(len(boards)): # all boards
            for j in boards[i]: # all rows
                if i in won:
                    continue

                isWon = [False, 0]

                for k in j: # all cols
                    if k[1] == int(num):
                        k[0] = 1

                if sum([a[0] for a in j]) == len(j): #check row
                    isWon = [True, num]
                else: #check col
                    for a in range(5):
                        col = []
                        for k in boards[i]:
                            col.append(k[a])
                        
                        if sum([a[0] for a in col]) == len(j):
                            isWon = [True, num]

                if isWon[0] == True:
                    winners.append([boards[i], int(isWon[1])])
                    won.append(i)

    return winners

wintables = searchBingo()

firstwon = wintables[0]
lastwon = wintables[-1]

print(firstwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in firstwon[0]))
print(lastwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in lastwon[0]))