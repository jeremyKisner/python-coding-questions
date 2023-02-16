
def miniMaxSum(arr):
    first = 0
    last = 0
    arr.sort()
    for i in arr[0:4]:
        first +=i
    for i in arr[-4:]:
        last += i
    print(first, last)


if __name__ == "__main__":
    arr = [7, 69, 2, 221, 8974]
    miniMaxSum(arr)
