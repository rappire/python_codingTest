import sys
from itertools import combinations

input = sys.stdin.readline

string = input().rstrip()
stack = []
bracket = []

for i, ch in enumerate(string):
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        close = stack.pop()
        bracket.append([close, i])

removeArr = []
for i in range(1, len(string) + 1):
    for j in combinations(bracket, i):
        stringArr = list(string)
        for x, y in j:
            stringArr[x] = ""
            stringArr[y] = ""
        removeArr.append("".join(stringArr))

removeArr = list(set(removeArr))
removeArr.sort()
for i in removeArr:
    print(i)
