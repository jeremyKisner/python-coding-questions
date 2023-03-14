
def kangaroo(x1, v1, x2, v2):
    for i in range(1, 10000):
        k1 = x1 + v1 * i
        k2 = x2 + v2 * i
        if k1 == k2:
            return "YES"
    return "NO"


if __name__ == "__main__":
    kangaroo(0, 3, 4, 2)