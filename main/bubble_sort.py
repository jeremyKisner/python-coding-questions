
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    my_arr = [6,1,8,4,9,7,3,2,5]
    bubble_sort(my_arr)
    my_arr = ['c','a','p','h','j','b']
    bubble_sort(my_arr)