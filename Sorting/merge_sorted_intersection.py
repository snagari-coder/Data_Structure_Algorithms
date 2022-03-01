def merge_sorted_no_duplicates(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            aux.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            aux.append(l2[j])
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux

print(merge_sorted_no_duplicates([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [2, 3, 5, 6, 7, 8, 9, 10]

def merge_sorted(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            aux.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            aux.append(l2[j])
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux
print(merge_sorted([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [2, 3, 5, 5, 6, 6, 7, 8, 8, 9, 10]

def intersect(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux
print(intersect([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [5, 6, 8]



