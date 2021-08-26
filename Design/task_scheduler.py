# Leetcode 621
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
# that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

        # (AAAABBB), n= 2 = A--A--A--A
        # Find max freq (=global_max), and number of elements who has max_freq(=count)
        # Take out the last A, there will be 3 groups, containing A + number of intervals
        # Hence the formula (global_max-1) * ( 1 + n ) + count
        # When n = 0, the formula gives a value less than length of input
        # hence take max of length of input and the formula

def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        global_max = 1
        count = 0
        
        for i in range(len(tasks)):
            if tasks[i] in hashmap:
                hashmap[tasks[i]] += 1
                global_max = max(global_max, hashmap[tasks[i]])
            else:
                hashmap[tasks[i]] = 1
        
        for value in hashmap.values():
            if value == global_max:
                count += 1
        
        return max(len(tasks), (global_max-1) * ( 1 + n ) + count)
     
        
        
