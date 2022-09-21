import heapq


class Solution:
    def reorganizeString(self, s):
        d = {}
        res = ""
        for char in s:
            d[char] = d.get(char, 0) + 1
        # using a priority queue
        pq = []
        heapq._heapify_max(pq)
        for k in d:
            pq.append([d[k], k])
            heapq._siftdown_max(pq, 0, len(pq) - 1)
        while len(pq) > 1:
            p1, p2 = heapq._heappop_max(pq), heapq._heappop_max(pq)
            res += p1[1]
            res += p2[1]
            p1[0] -= 1
            p2[0] -= 1
            if p1[0] > 0:
                pq.append(p1)
                heapq._siftdown_max(pq, 0, len(pq) - 1)
            if p2[0] > 0:
                pq.append(p2)
                heapq._siftdown_max(pq, 0, len(pq) - 1)
        if len(pq):
            if pq[0][0] == 1:
                res += pq[0][1]
            else:
                return ""
        return res
