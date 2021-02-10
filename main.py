from insertion_sort.basic_insertion_sort import insertion_sort



def main():
    # data to sort
    need_to_sort = [8,4,2,3,5,6,1]

    # run the algorithm
    insertion_sort(need_to_sort)

    # display sorted output
    print(f"\n\nSorted Result \t==>\t {need_to_sort}")

if __name__=='__main__':
    main()
