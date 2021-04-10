# Find the most frequently occuring item in an array
#Ex: [1,3,1,3,2,1] Ans = 1

def most_frequent(given_list):
    max_item = None
    hashmap = {}
    global_max = 1
    if len(given_list) == 0:
      return None
    for i in range(len(given_list)):
        if given_list[i] in hashmap:
            count = hashmap[given_list[i]]
            hashmap[given_list[i]] = count + 1
            if global_max < hashmap[given_list[i]]:
                global_max = hashmap[given_list[i]]
        else:
            hashmap[given_list[i]] = 1
            
    for key, value in hashmap.items():
        if value == global_max:
            max_item = key
    
    return max_item
