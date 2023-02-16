from random_generator import random_list


def single_looping(arr):
    for i in range(0, len(arr), 1):
        print(f"{i} -- {arr[i]}")


def double_looping(arr):
    for i in range(0, len(arr)):
        for j in range(i, 0, -1):
            print(j)


def single_enumeration(arr):
    for i, key in enumerate(arr):
        print(f"index {i} -- key {key}")


if __name__ == "__main__":
    my_arr = random_list()
    single_looping(my_arr)
    double_looping(my_arr)
    single_enumeration(my_arr)
