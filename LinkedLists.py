#!/usr/bin/env python

class Node(object):
    def __init__(self,value):
        self.item = value
        self.ref = None


class LinkedList(object):
    def __init__(self):
        self.start_node = None

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                current.next = new_element
        else: self.head = new_element

    def counter(self):
        count = 0
        if self.head:
            count +=1
            while current.next:
                count +=1
            current.next = new_element
        return count

def main():
    element1 = element(15)
    element2 = element(16)
    element2 = element(17)
    l1 = LinkedList(element1)
    l1.append(element2)
    l1.append(element3)
    print(l1.counter())
if __name__ == "__main__":
    main()
