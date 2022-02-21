# Leetcode 341

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nestedList):
            for nested_integer in nestedList:
                if nested_integer.isInteger():
                    self.integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList())
        self.integers = []
        self.position = -1
        flatten_list(nestedList)
    
    def next(self) -> int:
        self.position += 1
        return self.integers[self.position]
        
    
    def hasNext(self) -> bool:
        return (self.position + 1) < len(self.integers)
         
# Time complexity = 
# constructor = O(N+K), N = total number of integers in list, K = number of lists
# method next = O(1)
# method hasNext = O(1)
# Space complexity = O(N+D), D = depth of nested list
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
