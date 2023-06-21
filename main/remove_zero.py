

def remove_zeros_from_str(_input: str) -> str:
    _start = 0
    _end = len(_input) - 1
    for i in range(len(_input)):
        if _input[_start] == '0':
            _start += 1
        if _input[_end] == '0':
            _end -=1
    print('result: ', _input[_start:_end+1])


if __name__ == "__main__":
    remove_zeros_from_str("000123400000")
