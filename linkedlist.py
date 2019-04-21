#!/usr/bin/env python
from Box import Box

def countElementsInLinkedList(box):
    counter = 1
    current = box
    while current.Next is not None:
        current = current.Next
        counter = counter +1
    return counter

def main ():
    head = Box(9)
    box1 = Box(8)
    box2 = Box(7)
    box3 = Box(6)
    head.Next = box1
    box1.Next = box2
    box2.Next = box3
    print(countElementsInLinkedList(head))

if __name__ =="__main__":
    main()
