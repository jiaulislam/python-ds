def selection_sort(arr):

    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
        
        yield arr


# def max_selection_sort(arr):

#     for i in range(len(arr)):
#         max_pos = 0
#         for j in range(i-1,)