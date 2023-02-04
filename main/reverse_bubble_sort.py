from random_generator import random_list

def reverse_bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    my_arr = random_list()
    print(f"INPUT: {my_arr}")
    reverse_bubble_sort(my_arr)
    print(f"OUTPUT: {my_arr}")
