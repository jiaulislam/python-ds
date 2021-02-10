"""
The Insertion Sort is simple sorting algorithm with O(n^2) time complexity.
It always maintains a sorted sublist in the lower position of the list. 
Each new item is then "inserted" back to the previous sublist in such 
that the sorted sublist is one item larger.
"""


from typing import List, NoReturn


def insertion_sort(data_to_sort: List) -> NoReturn:

    global ForCounter, WhileCounter
    # need_to_sort = [8, 4, 2, 4, 5, 6, 1]
    for index in range(1, len(data_to_sort)):
        key = data_to_sort[index] # 4
        sorted_position = index-1 # 0

        while sorted_position >= 0 and key < data_to_sort[sorted_position]:
            # Swap the smaller value with compared index value
            data_to_sort[sorted_position + 1] = data_to_sort[sorted_position] 
            sorted_position -= 1

        data_to_sort[sorted_position + 1] = key

 
# 1st random number sorting ->  6.154s
# 2st random number sorting ->  6.296s
# 3st random number sorting ->  6.214s
# 4st random number sorting ->  6.847s
# 5st random number sorting ->  5.578s
