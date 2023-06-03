def is_balance(item):
    s = list()

    for i in item:
        print(i)
        if i == "(":
            s.append(i)
        if i == ")":
            if not s:
                return False
            s.pop()
    return not s 

if __name__ == "__main__":
    a = input()

    if is_balance(a):
        print(a," is balanced")
    else:
        print(a, " is not balanced")