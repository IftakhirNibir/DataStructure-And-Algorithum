import collections
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
print(not stack)