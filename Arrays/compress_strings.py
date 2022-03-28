import collections
def compress(s):
    d = collections.defaultdict(int)
    for i in s: #This doesnt work for ABAAAABBBCCC, this doesnt compress but count the characters
        d[i]+=1
    print (''.join(i+str(d[i]) for i in d))


def compress1(s):
    r = ''
    l = len(s)
    if l == 0:
        return ''
    if l == 1:
        return s+'1'
    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i-1]:
            cnt +=1
        else:
            r= r+s[i-1] + str(cnt)
            cnt = 1
        i+=1
    r = r+s[i-1] + str(cnt)
    print(r)


compress1('AAAAABBBBCCCC')
compress1('ABAAAABBBCCC')