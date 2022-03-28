def finder1(l1,l2):
    l1.sort()
    l2.sort()
    for i in l1:
        if i not in l2:
            print(i)

def finder2(l1,l2):
    l1.sort()
    l2.sort()
    for num1,num2 in zip(l1,l2):
        if num1 != num2:
            return num1
    return l1[-1] #else return last element

import collections
def finder3(arr1,arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] +=1
    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1

def finder4(arr1,arr2):
    result = 0
    #perform XOR between numbers of array
    for num in arr1+arr2:
        result = result ^ num
        print(result)
    return result
finder4([1,2,3,4,5,6,7],[3,7,2,1,4,6])

