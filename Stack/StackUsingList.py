stack = []
def push():
    if length==len(stack):
        print("Stack is full")
    else:
        element = int(input("Enter the value: "))
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("Stack is already empty!")
    else:
        e = stack.pop()
        print(f"You remove {e} element from Stack")
        print(stack)

length = int(input("Enter the stack limit: "))
while True:
    print("Select the opearation: \
          1 for push, 2 for pop and 3 for quit")
    choice = int(input("Enter the option: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct option carefully!")