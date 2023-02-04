from random_generator import random_list

def single_looping(arr):
    for i in range(0, len(my_arr), 1):
        print(f"{i} -- {arr[i]}")

def double_looping(arr):
    for i in range(0, len(my_arr), ):
        for j in range(i, 0, -1):
            print(j)


if __name__ == "__main__":
    my_arr = random_list()
    single_looping(my_arr)
    double_looping(my_arr)
