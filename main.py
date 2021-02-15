from random import random
from typing import List
from binary_search.basic_bs import binary_search



# def style_print(array: List):
#     row = 0
#     for i in range(len(array)):
#         if row == 10:
#             row = 0
#             print("\n")
#         print(f"{array[i]}", end="\t")
#         row += 1



def main():
    m = [1,2,4,5,6,7,8,9,10]
    
    result = binary_search(m, 10)
    print(result)

if __name__=='__main__':
    print("Hello World")
    main()
