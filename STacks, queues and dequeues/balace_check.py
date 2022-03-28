def balance_check(s):
    arr = []
    for i in s:
        if i in ['(','[','{',]:
            arr.append(i)
        if i == ')':
            if arr == [] or arr.pop() != '(':
                return False

        if i == '}':
            if arr == [] or arr.pop() != '{':
                return False
        if i == ']':
            if arr == [] or arr.pop() != '[':
                return False
    return len(arr) == 0

def balance_check1(s):
    if len(s)%2 != 0: #if no spaces or words
        return False
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack)== 0:
                return False
            last_open = stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0


print(balance_check('[](){([[[]]])}'))
print(balance_check1('[](){([[[]]])}()['))
print(balance_check('[](){([[[]]])}'))