# Old Norse Alphabet

Old Norse Alphabet & sorting in Python

### Motivation

Old Norse constains letters that may be hard to type with most keyboards. Prime examples being þ, ð and ǫ. There are also some letters "missing", like c and q. This package offers the alphabet & tricky individual letters as constants.

Also provides sorting function to get the old norse alphabet order just right.

### Install

`pip install old-norse-alphabet`


### Usage

The library offers Old Norse alphabet in lower/uppercases, and a function for sorting by old norse alphabetical order.


#### Sort

The crate exposes custom compare function for getting old norse alphabetical order just right. Compare function accepts two words to compare, so you can use cmp_to_key with sorted. 

```python
from functools import cmp_to_key
from old_norse_alphabet.sort import old_norse_sort

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

result = sorted(words, key=cmp_to_key(old_norse_sort))

print(result)
# "aðili", "á-auki", "áðr", "áfir", "ef-lauss", "él-ligr", "madr", "maðka", "maðr", "mæðr", "ógnan", "þakkan", "æðrask", "œgir", "öðli",

```

#### Alphabet

Alphabets are just immutable tuples of letters in ON alphabetical order with getter functions.

```python
from old_norse_alphabet import alphabet

# Both alphabets contain 34 characters.
upper = alphabet.get_upper() 
lower = alphabet.get_lower()

# There is special list for characters that are valid as first letter.
valid_as_first = alphabet.get_valid_as_first()

```

Exposed special characters:

```python
from old_norse_alphabet import alphabet

print(alphabet.eth) # ð
print(alphabet.thorn) # þ
print(alphabet.o_caudata) # ǫ
print(alphabet.slashed_o) # ø
print(alphabet.ae) # æ
print(alphabet.oe) # œ
print(alphabet.ash) # Alternative export of AE

```

### About Old Norse

[Old Norse](https://en.wikipedia.org/wiki/Old_Norse) was a North Germanic language that was spoken by inhabitants of Scandinavia and their overseas settlements from about the 7th to the 15th centuries.
