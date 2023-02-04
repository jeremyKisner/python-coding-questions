from bubble_sort import bubble_sort
from random_generator import random_list


def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print(f"Item found? {found}")
    return found


if __name__ == "__main__":
    my_arr = random_list()
    print(f"INPUT: {my_arr}")
    my_arr = bubble_sort(my_arr)
    print(f"SORTED: {my_arr}")
    search_key = input("what do you want to look for? ")
    binary_search(my_arr, int(search_key))