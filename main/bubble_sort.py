import time
from main.random_generator import random_list

def bubble_sort(arr):
    t = time.process_time()
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    elapsed_time = time.process_time() - t
    print(f"bubble sort {elapsed_time}")
    return arr

if __name__ == "__main__":
    my_arr = random_list()
    print(f"INPUT: {my_arr}")
    bubble_sort(my_arr)
    print(f"OUTPUT: {my_arr}")
