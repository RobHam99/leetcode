from collections import deque

class RecentCounter:
    def __init__(self, ):
        self.queue = deque()
        
    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        
        return len(self.queue)
    
obj = RecentCounter()
param_1 = obj.ping(1)