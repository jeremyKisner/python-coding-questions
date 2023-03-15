#!/bin/python3

#
# Complete the 'countApplesAndOranges' function below.

#  s and t are the length of house
#  s - start | t - end
#  a - Left apple tree | b -Right orange tree


def get_total_fruit(s: int , t: int, results: list) -> int:
    total = 0
    for fruit in results:
        if fruit >= s and fruit <= t:
            total += 1
    return total


def get_counts(fruit_tree: int, fruits: list) -> list:
    result = []
    for fruit in fruits:
        result.append(fruit+fruit_tree)
    return result


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_results = get_counts(a, apples)
    oranges_results = get_counts(b, oranges)
    print(apples_results, oranges_results)
    print(get_total_fruit(s, t, apples_results),
          get_total_fruit(s, t, oranges_results))


if __name__ == '__main__':
    s = 7
    t = 10
    a = 4
    b = 12
    apples = [2, 3, -4]
    oranges = [3, -2, -4]
    countApplesAndOranges(s, t, a, b, apples, oranges)
