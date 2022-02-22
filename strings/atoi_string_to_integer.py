#Leetcode 8 ( incomplete )
def atoi(str1):
    integer = 0
    sign = ''
    if str1[0] == '-':
        sign = "-"
        i = 1
    else:
        i = 0

    while i < len(str1):
        if 0 <= (ord(str1[i]) - ord('0')) < 9:
            # ord() func takes in a single length string/char as argument
            # and returns ASCII value of that char
            integer = integer * 10 + (ord(str1[i]) - ord('0'))
            i += 1
        else:
            return 'Invalid input'
    if sign == '-':
        return integer*-1
    else:
        return integer


print(atoi("-134"))
print(atoi("-134a"))
