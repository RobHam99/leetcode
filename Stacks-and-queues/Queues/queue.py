import collections as col

queue = col.deque()

queue = col.deque([1, 2, 3])

queue.append(4)

queue.append(5)

queue.popleft()
queue.popleft()

queue[0]
len(queue)