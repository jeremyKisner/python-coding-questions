
def linear_search(data, item):
    isFound = False
    for i in data:
        if i == item:
            isFound = True
            break
    return isFound


if __name__ == "__main__":
    my_arr = [5, 4, 9, 2, 0, 1, 7]
    print(linear_search(my_arr, 9))
    print(linear_search(my_arr, 6))
