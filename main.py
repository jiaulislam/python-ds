from random import random
from insertion_sort.basic_insertion_sort import insertion_sort
from random import shuffle


def main():
    # data to sort
    need_to_sort = []

    for ranadom in range(1,10000):
        need_to_sort.append(ranadom)
    
    shuffle(need_to_sort)

    print(f"\n\nGiven Array \t==>\t {need_to_sort}")

    # run the algorithm
    insertion_sort(need_to_sort)

    # display sorted output
    print(f"\n\nSorted Array \t==>\t {need_to_sort}")

if __name__=='__main__':
    main()
