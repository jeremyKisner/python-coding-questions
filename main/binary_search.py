from bubble_sort import bubble_sort

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
    return found


if __name__ == "__main__":
    my_arr = [5, 2, 6, 9, 3]
    my_arr = bubble_sort(my_arr)
    print(binary_search(my_arr, 2))