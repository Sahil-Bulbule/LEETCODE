class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        order = sorted(range(n), key=servers.__getitem__)  # servers by weight, then index
        free = list(range(n))  # ranks in that order; sorted list is already a heap

        ans, busy = [], []  # busy: (second it frees up) * n + rank
        for s, t in enumerate(tasks):
            while busy and busy[0] < (s + 1) * n:  # done by second s
                heappush(free, heappop(busy) % n)
            start, r = (s, heappop(free)) if free else divmod(heappop(busy), n)  # none free: the first to finish takes it
            heappush(busy, (start + t) * n + r)
            ans.append(order[r])

        return ans