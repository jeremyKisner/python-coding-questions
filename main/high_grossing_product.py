
test_data = [
    "ID,PRICE_PER_UNIT,DATE"
    "1A,64,2023/01/01",
    "1C,100,2023/01/02",
    "1A,64,2023/01/02",
    "1B,45,2023/01/01",
    "1A,64,2022/12/01",
    "1B,47,2022/12/01",
    "1C,100,2022/11/02",
    "1A,41,2022/11/01",
    "1B,29,2022/11/15",
    "1B,29,2022/11/16",
    "1B,29,2022/11/17",
    "1B,39,2022/11/01",
    "1A,50,2022/12/15",
]


def process():
    result = {}
    for index in range(1, len(test_data) - 1):
        data = test_data[index].split(",")
        if data[0] not in result:
            result.update({data[0]: int(data[1])})
        else:
            price = result.get(data[0])
            result.update({data[0]: int(data[1]) + price})
    print(f"totals: {result}")
    product = max(result, key=result.get)
    records = [test_data[i] for i in range(1, len(test_data) - 1)
                if test_data[i].split(",")[0] == product]
    print(f"records {records}")


if __name__ == "__main__":
    process()
