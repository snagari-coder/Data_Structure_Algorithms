# A queue is implemented with two stacks ( stacks are implemented with arrays : q_array, s_array )
# All enqueueing happens in s_array, and for dequeueing:
# First check if q_array is empty, if empty, pop all elements from s_array and push into q_array. Pop the topmost element from q_array
# If q_array is not empty, pop the top most element from q_array.


class QueuesWithStacks:
    def __init__(self):
        self.q_array = []
        self.s_array = []
        self.length = 0

    def enqueue(self, value):
        self.s_array.append(value)

    def dequeue(self):
        if len(self.q_array) == 0:
            if len(self.s_array) == 0:
                return "Queue is empty"
            else:
                for i in range(0, len(self.s_array)):
                    self.q_array.append(self.s_array.pop())
                return self.q_array.pop()
        else:
            return self.q_array.pop()

    def peek(self):
        if len(self.q_array) == 0:
            if len(self.s_array) == 0:
                return "Queue is empty"
            else:
                for i in range(0, len(self.s_array)):
                    self.q_array.append(self.s_array.pop())
                return self.q_array[len(self.q_array) - 1]
        else:
            return self.q_array[len(self.q_array) - 1]

    def print_queue(self):
        if len(self.s_array) == 0:
            if len(self.q_array) == 0:
                print("Queue is empty")
            else:
                for i in range(len(self.q_array) - 1, -1, -1):
                    print(self.q_array[i])
        else:
            if len(self.q_array) == 0:
                print("Queue is empty")
            else:
                for i in range(len(self.q_array) - 1, -1, -1):
                    print(self.q_array[i])
            for i in range(0, len(self.s_array)):
                print(self.s_array[i])


my_queue = QueuesWithStacks()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)

print("First element of queue is: ", my_queue.peek())
print("Dequeued element is: ", my_queue.dequeue())
print("First element of queue is: ", my_queue.peek())
my_queue.enqueue(6)
my_queue.print_queue()
print("Dequeued element is: ", my_queue.dequeue())
print("Dequeued element is: ", my_queue.dequeue())
print("Dequeued element is: ", my_queue.dequeue())
print("Dequeued element is: ", my_queue.dequeue())
print("Dequeued element is: ", my_queue.dequeue())
print("Dequeued element is: ", my_queue.dequeue())
