from collections import deque

stack = deque()

quantity = int(input())
for _i in range(quantity):
    cmd = input().split()
    if cmd[0] == "POP":
        stack.pop()
    elif cmd[0] == "PUSH":
        stack.append(cmd[1])

for _i in range(len(stack)):
    print(stack.pop())
