import pandas as pd

input = {
    "name":   ['a', 'b', 'c', 'd', 'e'],
    "id":     [1, 2, 3, 4, 5],
    "active": [True, False, True, True, False]
}


def load():
    df = pd.DataFrame(input)
    exclude = (df["active"] == True)
    return df[exclude]


if __name__ == "__main__":
    print(load())
