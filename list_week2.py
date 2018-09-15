my_list1 = [0, 3, 6, 9, 10, 2, 5] 
my_list2 = [2, 6, 4, 7, 8, 1, 15]
my_new_list=[]
for idx in range(len(my_list1)):
    for idx2 in range(len(my_list2)):
        if my_list1[idx] == my_list2[idx2]:
            my_new_list.append(my_list1[idx])
my_new_list.sort()
print (my_new_list)