l=list(map(int, open("1.txt")))

#part 1
print(sum(a<b for a,b in zip(l,l[1:])))

#part 2
print(sum(a<b for a,b in zip(l,l[3:])))