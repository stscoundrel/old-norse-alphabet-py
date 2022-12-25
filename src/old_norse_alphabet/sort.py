from .alphabet import SortingAlphabet, get_sorting_alphabet

not_found = 404


def compare(a: str, b: str, index: int, alphabet: SortingAlphabet) -> int:
    if a.lower() == b.lower():
        return 0

    if len(a) <= index:
        return -1

    if len(b) <= index:
        return 1

    try:
        index_a = alphabet.index(a[index].lower())
    except ValueError:
        index_a = not_found

    try:
        index_b = alphabet.index(b[index].lower())
    except ValueError:
        index_b = not_found

    if index_a == not_found and index_b != not_found:
        return 1

    if index_b == not_found and index_a != not_found:
        return -1

    if index_a == index_b:
        new_index = index + 1
        return compare(a, b, new_index, alphabet)

    return index_a - index_b


def old_norse_sort(a: str, b: str) -> int:
    alphabet = get_sorting_alphabet()

    return compare(a, b, 0, alphabet)
