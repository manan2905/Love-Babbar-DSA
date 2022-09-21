# code
import heapq


def rearrange(s):
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
    pq = []
    heapq._heapify_max(pq)
    for k in d:
        pq.append([d[k], k])
        heapq._siftdown_max(pq, 0, len(pq) - 1)
    while len(pq) > 1:
        p1, p2 = heapq._heappop_max(pq), heapq._heappop_max(pq)
        minz = min(p1[0], p2[0])
        p1[0] -= minz
        p2[0] -= minz
        if p1[0] > 0:
            pq.append(p1)
            heapq._siftdown_max(pq, 0, len(pq) - 1)
        if p2[0] > 0:
            pq.append(p2)
            heapq._siftdown_max(pq, 0, len(pq) - 1)
    if len(pq):
        if pq[0][0] == 1:
            return 1
        else:
            return 0
    return 1


t = int(input())
for _ in range(t):
    s = input()
    print(rearrange(s))
