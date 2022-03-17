from collections import deque

read_books = deque()
stack = deque()

quantity = int(input())
for _i in range(quantity):
    cmd = input()
    if cmd[:4] == "READ":
        read_books.appendleft(stack.pop())
    elif cmd[:3] == "BUY":
        stack.append(cmd[4:])

for _i in range(len(read_books)):
    print(read_books.pop())
