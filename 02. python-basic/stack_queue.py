from collections import deque

# stack : 먼저 들어갈수록 나중에 나옴.

a = []
a.append(0)
a.pop()

# queue : 먼저 들어갈수록 먼저 나옴.

b = []
b.append(0)
b.pop(0)

# stack queue
# deque를 이용해서 양방향 처리가 가능

c = deque()
c.append(1)
print(c)
c.appendleft(2)
print(c)
c.pop()
print(c)
c.popleft()
print(c)