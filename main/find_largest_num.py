
def find_largest_num(input: list):
    largest_num = None
    if input and type(input) == list:
        for num in input:
            if type(num) != int:
                continue
            if not largest_num:
                largest_num = num
            elif largest_num < num:
                largest_num = num
    return largest_num
