from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

# your code here
quantity = int(input())
for i in range(quantity):
    cmd = input().split()
    if cmd[0] == "TAKE":
        if len(candy_bag) > 0:
            print(candy_bag.pop())
        else:
            print("We are out of candies :(")
    elif cmd[0] == "PUT":
        candy_bag.append(cmd[1])
