
def reverse_integer(int_to_reverse: int):
    reversed = None
    if type(int_to_reverse) == int:
        reversed = int(str(int_to_reverse)[::-1])
    return reversed
