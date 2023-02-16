def timeConversion(s:str):
    arr = s.split(":")

    if "AM" in arr[2] and int(arr[0]) == 12:
        arr[0] = "00"
    elif "AM" in arr[2]:
        arr[0] = f"{int(arr[0]) :02d}"
    elif "PM" in arr[2] and int(arr[0]) < 12:
        arr[0] = f"{int(arr[0]) + 12}"
    
    arr[2] = arr[2].replace("AM", "")
    arr[2] = arr[2].replace("PM", "")
    return ":".join(arr)


if __name__ == "__main__":
    result = timeConversion("7:00:00PM")
    print(result)
