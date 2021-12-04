lines = [i.replace("\n", "") for i in open("2.txt").readlines()]

#       h  d
pos1 = [0, 0]
#       h  d  a
pos2 = [0, 0, 0]

for i in lines:
    num = int(i[-1:])

    if i.startswith("f"):
        #part 1
        pos1[0] += num

        #part 2
        pos2[0] += num
        pos2[1] += pos2[2] * num
    else:
        #part 1
        pos1[1] += -num if i.startswith("u") else num

        #part 2
        pos2[2] += -num if i.startswith("u") else num

print(pos1, pos1[0] * pos1[1])
print(pos2, pos2[0] * pos2[1])