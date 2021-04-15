#Write a functon that takes two strings and returns True if they are one away from each other
#They are one away from each other if a single operation (changing a character, deleting a character
# adding a character ) will change one of the strings to the other.
# Ex: abcde, abcd are one away. 
# Implement your function below.
def is_one_away(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    count = 0
    i,j = 0,0
    
    if abs(n1-n2) > 1:
        return False
    else:
        if n1 == n2:
            while i < n1 and count < 2:
                if s1[i] == s2[i]:
                    i += 1
                else:
                    count += 1
                    i += 1
            if count > 1:
                 return False
            else:
                 return True
        if n1 > n2 :
            while i < n1 and j < n2 and count < 2:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    count += 1
                    i += 2
                    j += 1
            if count > 1:
                return False
            else:
                return True
        if n1 < n2 :
            while i < n1 and j < n2 and count < 2:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    count += 1
                    j += 2
                    i += 1
            if count > 1:
                return False
            else:
                return True
            
#Time complexity = O(n)

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
