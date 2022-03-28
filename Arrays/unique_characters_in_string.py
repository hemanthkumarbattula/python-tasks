import collections
def unique_char(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            return False

    return True

def unique_char1(s):
    return len(set(s)) == len(s)

def unique_char2(s):
    char = set()
    for let in s:
        if let in char:
            return False
        else:
            char.add(let)
    return True

print(unique_char('abcde'))
print(unique_char('aabc'))
print(unique_char('abcdde'))

