import time

def insertion_sort(arr: list):
    t = time.process_time()
    for item in range(1, len(arr)):
        index = item
        while arr[index - 1] > arr[index] and index > 0:
            arr[index - 1], arr[index] = arr[index], arr[index - 1]
            index -= 1
    elapsed_time = time.process_time() - t
    print(f"insertion sort {elapsed_time}")
    return arr

if __name__ == "__main__":
    my_arr = [4,3,7,1,9,2]
    print(f"IN {my_arr}")
    print(f"OUT {insertion_sort(my_arr)}")