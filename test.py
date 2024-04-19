def rotate_left(my_list: list, k: int) -> list:
    s = 0
    for i in range(k):
        s = my_list[0]
        for j in range(len(my_list)-1):
            my_list[j] = my_list[j+1]
        my_list[-1] = s  
    return my_list

print(rotate_left([1, 2, 3, 4, 5], 2))