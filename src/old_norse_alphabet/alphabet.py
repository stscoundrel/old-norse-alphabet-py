from typing import Tuple

AlphabetList = Tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]
CombinedAlphabet = Tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]
ValidFirsts = Tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]
SortingAlphabet = Tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]

alphabet_upper = (
    "A",
    "Á",
    "B",
    "D",
    "Ð",
    "E",
    "É",
    "F",
    "G",
    "H",
    "I",
    "Í",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "Ó",
    "P",
    "R",
    "S",
    "T",
    "U",
    "Ú",
    "V",
    "W",
    "Y",
    "Ý",
    "Þ",
    "Æ",
    "Ǫ",
    "Ø",
    "Œ",
)
alphabet_lower = (
    "a",
    "á",
    "b",
    "d",
    "ð",
    "e",
    "é",
    "f",
    "g",
    "h",
    "i",
    "í",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ó",
    "p",
    "r",
    "s",
    "t",
    "u",
    "ú",
    "v",
    "w",
    "y",
    "ý",
    "þ",
    "æ",
    "ǫ",
    "ø",
    "œ",
)
valid_as_first = (
    "a",
    "á",
    "b",
    "d",
    "e",
    "é",
    "f",
    "g",
    "h",
    "i",
    "í",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ó",
    "p",
    "r",
    "s",
    "t",
    "u",
    "ú",
    "v",
    "y",
    "ý",
    "þ",
    "æ",
    "ǫ",
    "ø",
    "œ",
)

# Additional non-standard letters & signs needed for sorting.
additional_chars = "ö", "x", "z"

# Additional signs that should get priority in sorting
priority_signs = "-", "_"

eth = "ð"
thorn = "þ"
o_caudata = "ǫ"
ash = "æ"
ae = "æ"  # alternative name
slashed_o = "ø"
oe = "œ"


def get_lower() -> AlphabetList:
    return alphabet_lower


def get_upper() -> AlphabetList:
    return alphabet_upper


def get_valid_as_first() -> ValidFirsts:
    return valid_as_first


def get_alphabet() -> CombinedAlphabet:
    return alphabet_lower + alphabet_upper


def get_sorting_alphabet() -> SortingAlphabet:
    return priority_signs + get_lower() + additional_chars
