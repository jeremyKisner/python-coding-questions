def binary_retrieval(arr, item):
    first = 0
    last = len(arr) - 1
    found = []
    while first <= last:
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            found.append(arr[midpoint])
            if item == arr[midpoint - 1]:
                x = arr[:midpoint]
                for i in range(len(x) - 1, -1, -1):
                    if x[i] == item:
                        found.append(x[i])
                    else:
                        break
            if item == arr[midpoint + 1]:
                x = arr[midpoint+1:]
                for i in range(len(x)):
                    if x[i] == item:
                        found.append(x[i])
                    else:
                        break
            break
        else:
            if item <= arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print(f"total {item} found: {found}")
    if found:
        return found
