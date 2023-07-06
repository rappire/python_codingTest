import sys
from collections import Counter

input = sys.stdin.readline


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

subArrA = []
subArrB = []


for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        subArrA.append(temp)

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        subArrB.append(temp)

arrDictA = Counter(subArrA)
print(arrDictA)
answer = 0

for i in subArrB:
    temp = T - i
    answer += arrDictA[temp]

print(answer)
