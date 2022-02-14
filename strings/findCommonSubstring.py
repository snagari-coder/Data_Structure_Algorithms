# given two strings 'abcdef', 'defghi', find a common substring = 'def'

def compare_string(s1, s2):
    if s1 == '' or s2 == '':
        return ''
    res = []
    hash = {}
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)):
        if s1[i].isalpha():
            hash[s1[i]] = 1 + hash.get(s1[i], 0)

    for c in s2:
        if c in hash and hash[c] > 0:
            res.append(c)
            hash[c] -= 1

    return "".join(res)


print(compare_string('abcdef', 'defghi'))
print(compare_string('abc1def', 'defghi'))
print(compare_string('abcddef', 'defghi'))
print(compare_string('abcddef', 'ddefghi'))
print(compare_string('abcDEF', 'defghi'))
print(compare_string('', 'defghi'))
print(compare_string('abcdef', ''))
print(compare_string('', ''))
