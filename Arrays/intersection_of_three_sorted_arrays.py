# Better handles duplicates
# Leetcode 1213

def intersection_of_three_sorted_arrays(a1, a2, a3):
    thisset = set()  # declaration of set
    # set is unordered, unchanged and can't have duplicates
    # set elements can't be indexed
    i, j = 0, 0

    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            thisset.add(a1[i])
            i += 1
            j += 1
        elif a1[i] > a2[j]:
            j += 1
        else:
            i += 1
    inter_list = list(thisset)  # since set can't be indexed, converting set into list
    thisset = set() # no need to declaring new variables
    i, j = 0, 0     # re-initialize the old variables
    while i < len(inter_list) and j < len(a3):
        if inter_list[i] == a3[j]:
            thisset.add(inter_list[i])
            i += 1
            j += 1
        elif inter_list[i] < a3[j]:
            i += 1
        else:
            j += 1
    return thisset


############################################################################################################################
def intersection_of_three_sorted_arrays(a1,a2,a3):
    i,j,k = 0,0,0
    result = []
    result_final = []

    if (len(a1) or len(a2) or len(a3)) == 0:
        return -1
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            result.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1

    i,j = 0,0
    while i < len(result) and j < len(a3):
        if result[i] == a3[j]:
            result_final.append(result[i])
            i += 1
            j += 1
        elif result[i] < a3[j]:
            i += 1
        else:
            j += 1
    
    if len(result_final) == 0:
        return -1
    else:
        return result_final

print(intersection_of_three_sorted_arrays([2,5,10],[2,3,4,10],[2,4,10]))
