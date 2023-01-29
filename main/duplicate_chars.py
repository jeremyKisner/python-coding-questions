
def check_for_duplicate_chars(input: str):
    containsDuplicates = False
    if input:
        previous_char = None
        for char in [*input]:
            if not previous_char:
                previous_char = char
            elif previous_char == char:
                containsDuplicates = True
            else:
                previous_char = char
    return containsDuplicates
