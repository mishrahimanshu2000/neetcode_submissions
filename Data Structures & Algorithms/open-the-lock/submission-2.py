class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if target in seen or '0000' in seen:
            return -1
        def get_next(lock):
            res = []
            for i in range(4):
                pos = str((int(lock[i]) + 1) % 10)
                neg = str((int(lock[i]) + 9 ) % 10)
                yield lock[:i] + pos + lock[i+1:]
                yield lock[:i] + neg + lock[i+1:]

        q = deque()
        q.append(('0000', 0))
        while q:
            lock, step = q.popleft()
            if lock == target:
                return step
            for new_lock in get_next(lock):
                if new_lock in seen:
                    continue
                q.append((new_lock, step+1))
                seen.add(new_lock)

        return -1        
