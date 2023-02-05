
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def do_math(func):
    m = func(2,2)
    print(f'did math - {m}')


if __name__ == "__main__":
    do_math(add)
    do_math(sub)
