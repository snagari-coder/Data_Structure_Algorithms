# code to generate a hash from base62 algorithm:
def base62_encode(deci):
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hash_str = ''
    while deci > 0:
        print(deci % 62)
        hash_str = s[int(deci % 62)] + hash_str
        deci /= 62
    #print(len(hash_str))
    return hash_str

print(base62_encode(999))
