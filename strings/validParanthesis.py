
# Leetcode 20
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen = {'}':'{', ']':'[',')':'('} # This hashmap contains closing and corresponding opening
                                                 # brackets
        
        for c in s:
            if c in closeToOpen: # if the bracket matches the key of hashmap
                if stack and stack[-1] == closeToOpen[c]: # check if stack is non empty, stack[-1] is the top
                                                          # of the stack
                    stack.pop()
                else:
                    return False # if there is a closing bracket before its corresponding opening bracket
                                 # then return False
            else:
                stack.append(c) # add all the opening brackets to the stack
        return True if not stack else False # if stack is empty at the end, found all matching braces
    
    # Time = space = O(n)
