
def anagram1(s1, s2):
    count = 0
    s1=s1.lower();s2=s2.lower()
    s1=s1.replace(' ','')
    s2=s2.replace(' ','')
    if len(s1)!= len(s2):
        return False
    for i in s1:
        if i in s2:
            count +=1
    if count == len(s1):
        return True
    else:
        return False

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

def anagram3(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
    return True
print(anagram1('dog', 'God'))
print(anagram2('clint eastwood', 'old west action'))
print(anagram3('aa', 'bb'))