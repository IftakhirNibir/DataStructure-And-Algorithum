def isValid(s):
    a = []
    d = 0

    for i in s:
        if i =='(':
            a.append(i)
        if i ==')':
            if not a:
                d=1
            if a:
                a.pop()
        
        if i =='{':
            a.append(i)
        if i =='}':
            if not a:
                d=1
            if a:
                a.pop()

        if i =='[':
            a.append(i)
        if i ==']':
            if not a:
                d=1
            if a:
                a.pop()

    if (not a) and d==0:
        return "True"
    else:
        return "False"

a = "(]"
print(isValid(a))
