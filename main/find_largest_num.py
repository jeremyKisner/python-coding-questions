
def find_largest_num(data_input: list):
    largest_num = None
    if data_input and type(data_input) == list:
        for num in data_input:
            if type(num) != int:
                continue
            if not largest_num:
                largest_num = num
            elif largest_num < num:
                largest_num = num
    return largest_num
