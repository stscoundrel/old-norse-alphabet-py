from functools import cmp_to_key
from typing import Tuple
from src.old_norse_alphabet import sort


def assert_is_sorted(result: list[str], expected: Tuple[str, ...]) -> None:
    for index, word in enumerate(result):
        assert expected[index] == word


def test_sorts_by_old_norse_alphabet() -> None:
    words = (
        "öðli",
        "ógnan",
        "æðrask",
        "aðili",
        "þakkan",
        "áfir",
        "á-auki",
        "él-ligr",
        "maðka",
        "ef-lauss",
        "œgir",
        "áðr",
        "maðr",
        "madr",
        "mæðr",
    )
    expected = (
        "aðili",
        "á-auki",
        "áðr",
        "áfir",
        "ef-lauss",
        "él-ligr",
        "madr",
        "maðka",
        "maðr",
        "mæðr",
        "ógnan",
        "þakkan",
        "æðrask",
        "œgir",
        "öðli",
    )

    result = sorted(words, key=cmp_to_key(sort.old_norse_sort))
    assert_is_sorted(result, expected)


def test_sorts_with_identical_words() -> None:
    words = "aðili", "maðka", "þakkan", "maðka"
    expected = "aðili", "maðka", "maðka", "þakkan"

    result = sorted(words, key=cmp_to_key(sort.old_norse_sort))
    assert_is_sorted(result, expected)


def test_sorts_mixed_upper_and_lower_letters() -> None:
    words = "aðili", "maðka", "þakkan", "adal", "ADAL", "maðka"
    expected = "adal", "ADAL", "aðili", "maðka", "maðka", "þakkan"

    result = sorted(words, key=cmp_to_key(sort.old_norse_sort))
    assert_is_sorted(result, expected)


def test_word_length_applies_when_sorting() -> None:
    words = "aðild", "AÐAL", "abbast", "aðal-vellir", "AÐA", "abbindi"
    expected = "abbast", "abbindi", "AÐA", "AÐAL", "aðal-vellir", "aðild"

    result = sorted(words, key=cmp_to_key(sort.old_norse_sort))
    assert_is_sorted(result, expected)


def test_sorts_uncommon_and_loaned_letters() -> None:
    words = "Gerzkr", "ger", "hal-dreki", "ÆZLI", "gervi", "eyxn", "halzi", "æxling"
    expected = "eyxn", "ger", "gervi", "Gerzkr", "hal-dreki", "halzi", "æxling", "ÆZLI"

    result = sorted(words, key=cmp_to_key(sort.old_norse_sort))
    assert_is_sorted(result, expected)
