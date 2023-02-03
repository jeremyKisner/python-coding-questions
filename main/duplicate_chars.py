
def check_for_duplicate_chars(data_in: str):
    containsDuplicates = False
    if data_in:
        previous_char = None
        for char in [*data_in]:
            if not previous_char:
                previous_char = char
            elif previous_char == char:
                containsDuplicates = True
            else:
                previous_char = char
    return containsDuplicates
