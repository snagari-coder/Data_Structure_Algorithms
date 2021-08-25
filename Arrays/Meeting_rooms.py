# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],[s3,e3],...]
# Determine if a person can attend all the meetings.
# Leetcode 252

def meeting_intervals(list1):
    list1 = sorted(list1) # first sort the array based on the starting time.
    i = 0
    while i+1 < len(list1):
        if list1[i][1] > list1[i + 1][0]: # if the end time of one meeting is more than starting time of next meeting, then he can't attend 
            return False
        else:
            i += 1
    return True


print(meeting_intervals([[0,30],[5,10],[15,20]]))

'''
sorting a list of lists based on second element of sublists
check_list = [(2, 3), (3, 4), (4, 1), (1, 3)]
def take_second(elem):
    return elem[1]
print(sorted(check_list,key=take_second))

'''
