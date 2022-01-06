from src.old_norse_alphabet import alphabet


def test_upper_and_lower_contain_same_characters_in_same_order() -> None:
    upper = alphabet.get_upper()
    lower = alphabet.get_lower()

    for index, letter in enumerate(upper):
        assert letter == lower[index].upper()

    for index, letter in enumerate(lower):
        assert letter == upper[index].lower()


def test_valid_at_first_does_not_contain_eth() -> None:
    valid_as_first = alphabet.get_valid_as_first()

    for letter in valid_as_first:
        assert letter != "ð"
