from math import floor

def binary_search(sorted_records, find_item):
    left = 0
    right= len(sorted_records) - 1
    try:
        while left <= right:
            middle = floor((left+right)/2)
            if sorted_records[middle] < find_item:
                left = middle + 1
            elif sorted_records[middle] > find_item:
                right = middle - 1
            else:
                return middle
    except IndexError:
        raise IndexError
    return Exception(f"{find_item} not found in the records.")