
def is_leap(year):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0:
            is_leap = False
        if year % 400 == 0:
            is_leap = True
    return is_leap


if __name__ == "__main__":
    print(is_leap(1990))
    print(is_leap(2100))
