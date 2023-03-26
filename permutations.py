s = input()

if len(s)==1:
    print(s)
else:
    newString = [[]]

    newS = list(s)
    groups = [newS] * len(s)
    for i in groups:
        newString=[x+[y] for x in newString for y in i]
    permutations = [''.join(item) for item in newString]

    for i in permutations:
        print(i)
