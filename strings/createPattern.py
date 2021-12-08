'''
# Create a pattern like this:
ABBBA
ACCCA
ACCCA
ACCCA
ABBBA
'''
def createPattern(x):
    list_top_bottom = ['A']*(x+2)
    list_middle = ['A'] * (x + 2)
    for i in range(1,len(list_top_bottom)-1):
        list_top_bottom[i] = 'B'
    for i in range(1,len(list_middle)-1):
        list_middle[i] = 'C'

    print("".join(list_top_bottom))
    for i in range(x):
        print("".join(list_middle))
    print("".join(list_top_bottom))
createPattern(3)
