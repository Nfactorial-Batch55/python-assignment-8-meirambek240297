def is_sorted(my_list: list) -> bool:
    for i in range(len(my_list)-1):
        if my_list[i]>my_list[i+1]:
            return False
            break
    return True
    
    
    
    
    
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([]))
print(is_sorted([1]))
print(is_sorted([-1, -1, 0, 1, 2]))