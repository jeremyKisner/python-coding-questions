
def disorder(data_input: str):
    result = []
    if data_input:
        for i in range(len(data_input)):
            x = 2+i
            temp = data_input[::x]
            temp = temp.replace(" ", "")
            result.append(temp.strip())
    return "".join(result)


if __name__ == "__main__":
    print(disorder("This is something I want to make a little crazy"))
