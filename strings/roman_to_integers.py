
import re
def roman_to_integers(roman):

    valid = (bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman)))
    # I, X, C, M are ones
    # V, L, D are fives
    # Rules:
    # M can repeat any number of times. ^M{0,3} --> Starts with 0 to 3 M's
    # Ones cannot come before a bigger number more than 1 time. IV is allowed, but not IIV --> IX|IV|
    # Ones can be repeated not more than three times after a fives. VIII is allowed, but not VIIII --> C{0,3}
    # Fives cannot be repeated when they are in front of ones. VI is allowed, but not VVI --> D?
    # $ states that only match the when ends with (IX|IV|V?I{0,3})
    if valid is True:
        n = len(roman)
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result, previous = 0, 0
        for i in range(n - 1, -1, -1):
            if value[roman[i]] >= previous:
                result += value[roman[i]]
            else:
                result -= value[roman[i]]
            present = value[roman[i]]

        return result
    else:
        return 'Invalid roman number'


print(roman_to_integers('IIX'))
# Time complexity = O(n)
# Space complexity = O(1)


