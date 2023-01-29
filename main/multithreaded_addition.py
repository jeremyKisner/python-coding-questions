from concurrent.futures import ThreadPoolExecutor

MAX_THREADS = 100

def add(x: int, y: int):
    result = x + y
    return result


def process(list1, list2):
    results = []
    with ThreadPoolExecutor(max_workers = MAX_THREADS) as e:
        for first in list1:
            for second in list2:
                future = e.submit(
                    add,
                    first,
                    second
                )
                results.append(future.result())
    return results


if __name__ == "__main__":
    first_list = [i for i in range(1,1000)]
    second_list = first_list[::-2]
    response = process(first_list, second_list)
    print(f"Total numbers calculated: {len(response)}")
