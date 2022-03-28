def large_count_sum(arr):

    if len(arr) == 0:
        return 0
    max_sum = cur_sum = arr[0]
    for i in arr[1:]:
        cur_sum = max (cur_sum +i, i)
        max_sum = max(cur_sum,max_sum)

    print(max_sum)

large_count_sum([1,2,-1,3,4,10,10,-10,-1]) #29
