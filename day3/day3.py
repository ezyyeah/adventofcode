lines = [i.replace("\n", "") for i in open("3.txt", "r").readlines()]

# part 1

bits = [""] * len(lines[0])

for i in range(len(lines)):
    for j in range(len(lines[i])):
        bits[j] += lines[i][j]

gamma = ""

for i in range(len(bits)):
    gamma += "1" if bits[i].count("1") > len(bits[i]) / 2 else "0"

print("multiply:", int(gamma, 2) * int(gamma.translate(str.maketrans("01", "10")), 2))

# part 2

lists = []

for i in range(2):
    clist = lines.copy()
    char = 0

    while len(clist) > 1:
        s = ("0" if i else "1") if [i[char] for i in clist].count("1") >= len(clist) / 2 or [i[char] for i in clist].count("1") == len(clist) - 1 else ("1" if i else "0")
        clist = [i for i in clist if i[char] == str(s)]
        char += 1
    
    lists.append(clist)

print(int(lists[0][0], 2) * int(lists[1][0], 2))
