import collections

expression = input()

stack = collections.deque()

for literal in expression:
    if literal == '(':
        stack.append('1')
    elif literal == ')':
        try:
            a = stack.pop()
        except IndexError:
            print("ERROR")
            break
else:
    if len(stack) == 0:
        print("OK")
    else:
        print("ERROR")
