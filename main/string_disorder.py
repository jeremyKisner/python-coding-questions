
def disorder(input: str):
    result = []
    if input:
        for i in range(len(input)):
            x = 2+i
            temp = input[::x]
            temp = temp.replace(" ", "")
            result.append(temp.strip())
    return "".join(result)


if __name__ == "__main__":
    print(disorder("This is something I want to make a little crazy"))
