tests = [[10, 1],
         [50, 2, 1, 9]]

numList = []
for x in tests:
    numList.append(sorted(x, key=lambda i: str(i) * 100, reverse=True))

for i in range(len(numList)):
    print(tests[i], ",the largest formed number is", "".join(map(str, numList[i])))