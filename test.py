from collections import defaultdict
 
def group_anagrams(words: list[str]) -> list[list[str]]:
    # printing original list
    print("The original list : " + str(words))
 
    # using defaultdict() + sorted() + values()
    # Grouping Anagrams
    temp = defaultdict(list)
    for ele in words:
        temp[str(sorted(ele))].append(ele)
    res = list(temp.values())
    return res
 
# print result
    #print("The grouped Anagrams : " + str(res))
   
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

# initializing list
#test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']