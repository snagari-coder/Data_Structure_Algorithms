def number_to_roman(x):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # 4,9,40,90,400,900 have a different representation, hence have to include in the look up array
    i = 12
    roman_numeral = ''
    while x != 0:
        if numbers[i] <= x:  # Finding the largest number less than or equal to x
            roman_numeral += romans[i]  # Add its equivalent in roman_numeral
            x -= numbers[i]  # subtract that number from the given number, until given number is reduced to zero
        else:
            i -= 1
    return roman_numeral


print(number_to_roman(49))
