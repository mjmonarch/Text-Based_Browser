n = int(input())

my_stack = [input() for x in range(n)]

for i in range(n):
    print(my_stack.pop())
