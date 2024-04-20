from collections import defaultdict

"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    # write your code here
    my_list.sort()
    print(my_list)
    c = 1
    b = 0
    for i in range(len(my_list)-1):
        if (my_list[i] + 1 == my_list[i+1]):
            c = c + 1
        elif (my_list[i] != my_list[i+1]) and (b<c):
                b = c
                c = 1
    if not my_list:
        return 0
    elif c>b:
        return c
    else:
        return b
    pass

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
     # write your code here
    my_list.sort()
    if (len(my_list)%3 == 0):
        for i in range(1, len(my_list)-1, 3):
            if (my_list[i-1] + 1 != my_list[i]):
                return my_list[i]-1
            elif (my_list[i]+1!=my_list[i+1]):
                return my_list[i]+1
    elif (len(my_list)%2==1):
        for i in range(1, len(my_list)-2, 3):
            if (my_list[i-1] + 1 != my_list[i]):
                return my_list[i]-1
            elif (my_list[i]+1!=my_list[i+1]):
                return my_list[i]+1
            elif(my_list[-2]+1!=my_list[-1]):
                return my_list[-1]-1
    elif (len(my_list)%2==0):
        for i in range(1, len(my_list), 2):
            if (my_list[i-1] + 1 != my_list[i]):
                return my_list[i]-1
        for i in range(1, len(my_list)-1, 2):
            if (my_list[i]+1!=my_list[i+1]):
                return my_list[i]+1
            else: 
                return my_list[0]-1
    elif not my_list:
        return None           
    pass


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    # write your code here
    my_list.sort()
    for i in range(len(my_list)-1):
        if my_list[i] == my_list[i+1]:
            return my_list[i]

    pass


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    # write your code here
    temp = defaultdict(list)
    for ele in words:
        temp[str(sorted(ele))].append(ele)
    res = list(temp.values())
    return res
    pass
