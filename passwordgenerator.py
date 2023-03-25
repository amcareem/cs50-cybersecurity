//Many phones are secured by a four-digit code.
//The most simple form of attack would be to “brute-force” type all possible passwords.
//There are 10,000 possible passwords when using a four-digit code.
//Following code is to generate all possible codes

//Expanding to eight characters, including upper and lowercase letters, numbers, and symbols, would result in 6,095,689,385,410,816 possible combinations.

from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + digits + punctuation, repeat=8):
    print(*passcode)
