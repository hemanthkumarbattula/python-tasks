def pair_sum1(arr,k):
    l = []
    arr1 = arr[:]
    for i in arr1:
        if k-i in arr:
            l.append((i,k-i))
            arr.remove(i)
            arr.remove(k-i)

    return len(l),l

def pair_sum2(arr,k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()
    for num in arr:
        target =  k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    return '\n'.join(map(str,list(output))), len(output)

print(pair_sum1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum2([1,3,2,2,2],4))