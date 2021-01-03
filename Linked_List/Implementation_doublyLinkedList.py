class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.previous = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current_node = self.head
            count = 0
            while count < index - 1:
                current_node = current_node.next
                count += 1
            new_node.next = current_node.next
            current_node.next.previous = new_node
            new_node.previous = current_node
            current_node.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            #self.head.previous = null
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.data != value:
                current_node = current_node.next

            if current_node.next is not None:
                current_node.next = current_node.next.next
                current_node.next.next.previous = current_node
                self.length -= 1
            else:
                print("The given value is not present in the linked list")

    def delete_by_index(self, index):
        count = 0
        current_node = self.head
        if self.head is None:
            print('The linked list is empty')
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return
        elif index >= self.length:
            print("The index is greater than the length of the linked list")
            return
        else:
            while count < index - 1:
                current_node = current_node.next
                count += 1
            current_node.next = current_node.next.next
            current_node.next.next.previous = current_node
            self.length -= 1
            if current_node.next is None:
                self.tail = current_node
            return

    def print_linked_list(self):

        if self.head is None:
            print("Linked list is empty")

        current_node = self.head
        all_linked_list_elements = []

        while current_node is not None:
            all_linked_list_elements.append(current_node.data)
            current_node = current_node.next

        print(all_linked_list_elements)


my_linkedList = doublyLinkedList()


my_linkedList.append(2)
my_linkedList.append(3)
my_linkedList.prepend(1)
my_linkedList.append(5)
my_linkedList.insert(3, 4)
my_linkedList.append(6)
my_linkedList.insert(7, 7)
my_linkedList.insert(0, 0)
my_linkedList.delete_by_value(99)
my_linkedList.delete_by_value(4)
my_linkedList.delete_by_value(4)
my_linkedList.delete_by_index(2)
my_linkedList.delete_by_index(2)
my_linkedList.print_linked_list()
