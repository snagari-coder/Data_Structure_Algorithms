class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def peek(self):
        if self.head is None:
            print("The queue is empty")
        else:
            print("The first in queue is: ", self.head.data)

    def dequeue(self):
        if self.head is None:
            print("The queue is empty")
        else:
            print("The popped element is: ", self.head.data)
            self.head = self.head.next
            self.length -= 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            self.tail = self.head
            self.length += 1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self.tail = new_node
            new_node.next = None
            self.length += 1

    def print_queue(self):
        all_queue_elements = []
        current_node = self.head
        while current_node is not None:
            all_queue_elements.append(current_node.data)
            current_node = current_node.next
        print(all_queue_elements)


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.peek()
my_queue.print_queue()
