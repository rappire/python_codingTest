import sys
from collections import deque

input = sys.stdin.readline

V = int(input())


def bfs(start):
    costArr = [-1 for _ in range(V + 1)]
    que = deque([start])
    costArr[start] = 0
    maxPos = -1
    maxCost = -1
    while que:
        now = que.popleft()
        for pos, cost in node[now]:
            if costArr[pos] == -1:
                que.append(pos)
                costArr[pos] = costArr[now] + cost
                if costArr[pos] > maxCost:
                    maxCost = costArr[pos]
                    maxPos = pos
    return maxPos, maxCost


node = [[] for i in range(V + 1)]
for i in range(1, V + 1):
    temp = list(map(int, input().split()))
    pos = temp[0]
    start = 1
    cost = 2
    while len(temp) > cost:
        node[pos].append([temp[start], temp[cost]])
        start += 2
        cost += 2

maxPos, maxCost = bfs(1)
maxPos, maxCost = bfs(maxPos)
print(maxCost)
