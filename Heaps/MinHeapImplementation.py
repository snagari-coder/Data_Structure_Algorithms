# Implementation of minimum Heap
# Finding the kth smallest element in an array/heap

import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Front = 1
        self.Heap = [0] * (self.maxsize+1)
        self.Heap[0] = -1 * sys.maxsize

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos//2
      
    # Function to return the position of left child for the node currently at pos
    def left_child(self, pos):
        return 2*pos
      
    def right_child(self, pos):
        return (2 * pos) + 1

    def is_leaf(self,pos):
        if self.size//2 <= pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def heapify(self, pos):
        if not self.is_leaf(pos):
            if self.Heap[pos] > self.Heap[self.left_child(pos)] or self.Heap[pos] > self.Heap[self.right_child(pos)]:
                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            print("Exceeded maxsize")
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.heapify(self.Front)
        return popped

    def minheap(self):
        for pos in range(self.size//2, 0, -1):
            self.heapify(pos)

    def print(self):
        for i in range(1, (self.size//2)+1):
            print("Parent: "+str(self.Heap[i]) + " Left Child:" + str(self.Heap[2*i]) + " Right Child:" + str(self.Heap[2*i + 1]))

    def kth_minimum(self,k):
        for i in range(0,k):
            result = self.remove()
        return result

myMinHeap = MinHeap(15)
myMinHeap.insert(5)
myMinHeap.insert(3)
myMinHeap.insert(17)
myMinHeap.insert(10)
myMinHeap.insert(84)
myMinHeap.insert(19)
myMinHeap.insert(6)
myMinHeap.insert(22)
myMinHeap.insert(9)
myMinHeap.minheap()
myMinHeap.print()
#print("The minimum element is: " + str(myMinHeap.remove()))
print("The 3rd smallest element in the array is: "+ str(myMinHeap.kth_minimum(3)))
