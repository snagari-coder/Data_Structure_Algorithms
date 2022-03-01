# Leetcode 252

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
            
        # Time = O(nlogn)
        # Space = O(1)
       
 #########################################################################################################
# Leetcode 253
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return None
        free_rooms = [] # this minheap stores the end timing of each meeting, with the min at the top
        intervals.sort(key=lambda x: x[0]) # sorting the list of lists based on first element
        heapq.heappush(free_rooms,intervals[0][1]) # adding the end time of first meeting
        for i in intervals[1:]: # starting from second meeting onwards
            if free_rooms[0] <= i[0]: #if the start time of the current meeting is more than the minheap top
                heapq.heappop(free_rooms) #pop the top of the minheap
            heapq.heappush(free_rooms,i[1]) # else push the endtime of the current meeting
        return len(free_rooms) # the length of the minheap is the number of rooms
        
        #Time = O(nlogn) for sorting
        # Space = O(n) for minheap
        
