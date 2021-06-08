def createStack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def pop(stack):
    if is_empty(stack):
        print("Error: Stack underflow")
    else:
        return stack.pop()

def push(stack,element):
    stack.append(element)

def find_next_greater(arr):
    stack = createStack()
    push(stack, arr[0])

    for i in range(1,len(arr)):
        next = arr[i]
        while not is_empty(stack):
            popped = pop(stack)
            if next > popped:
                print(str(popped) + "..." + str(next))
                continue
            else:
                push(stack,popped)
                break
        push(stack,next)

    while not is_empty(stack):
        popped = pop(stack)
        next = -1
        print(str(popped) + "..." + str(next))

find_next_greater([5,3,2,1,6,8,1,4,12,7,4])
#Time complexity = O(n)
#Space complexity = O(n)
