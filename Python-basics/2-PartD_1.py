a_list=list(range(1000,2001))
result_list=[]
for item in a_list:
    if item%7 == 0 and item%5 != 0:
        result_list.append(item)
print(result_list)
