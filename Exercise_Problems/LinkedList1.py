'''
__ProblemStatement__:
    Given two numbers in the form of linkedList, each digit represented by a node, add the two numbers and print in linked List form.
'''
class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_end(self,data):
        if self.head is None:
            newNode = Node(data,None,None)
            self.head = newNode
            self.tail = self.head
        else:
            newNode = Node(data,self.tail,None)
            self.tail.next = newNode
            self.tail = self.tail.next
            
    def insert_start(self,data):
        if self.head is None:
            newNode = Node(data,None,None)
            self.head = newNode
            self.tail = self.head
        else:
            newNode = Node(data,None,self.head)
            self.head.prev = newNode
            self.head = self.head.prev
            
            
    def PrintList(self):
        ptr = self.head
        if ptr:
            print("None <-> ",end="")
        while(ptr):
            print(ptr.val," <-> ",end="")
            ptr = ptr.next
        print("None",end="")
        
def AddNums(L1,L2):
    L3 = LinkedList()
    t1 = L1.tail
    t2 = L2.tail
    sum,carry = 0,0
    while(t1 and t2):
        sum = t1.val + t2.val + carry
        carry = sum//10
        sum = sum%10
        L3.insert_start(sum)
        sum = 0
        t1 = t1.prev
        t2 = t2.prev
    while(t1):
        sum = t1.val + carry
        carry = sum//10
        sum = sum%10
        L3.insert_start(sum)
        sum = 0
        t1 = t1.prev
    while(t2):
        sum = t2.val + carry
        carry = sum//10
        sum = sum%10
        L3.insert_start(sum)
        sum = 0
        t2 = t2.prev
    if carry:
        L3.insert_start(carry)
    return L3
        
if __name__ == "__main__":
    #Test with two empty linked lists:
    L1 = LinkedList()
    L2 = LinkedList()
    L3 = AddNums(L1,L2)
    L3.PrintList() # Expected output: None
    print()
    
    #Test with one empty linked list and one non-empty linked list:
    L1 = LinkedList()
    L2 = LinkedList()
    L2.insert_end(1)
    L2.insert_end(2)
    L2.insert_end(3)
    L3 = AddNums(L1,L2)
    L3.PrintList() # Expected output: None <-> 1  <-> 2  <-> 3  <-> None
    print()
    
    #Test with two non-empty linked lists of the same length:
    L1 = LinkedList()
    L1.insert_end(9)
    L1.insert_end(9)
    L1.insert_end(9)
    L2 = LinkedList()
    L2.insert_end(1)
    L2.insert_end(0)
    L2.insert_end(0)
    L3 = AddNums(L1,L2)
    L3.PrintList() # Expected output: None <-> 1  <-> 0  <-> 0  <-> 9  <-> None
    print()
    
    #Test with two non-empty linked lists of different lengths:
    L1 = LinkedList()
    L1.insert_end(9)
    L1.insert_end(9)
    L1.insert_end(9)
    L2 = LinkedList()
    L2.insert_end(1)
    L2.insert_end(0)
    L3 = AddNums(L1,L2)
    L3.PrintList() # Expected output: None <-> 1  <-> 0 <-> 0 <-> 8  <-> None
    print()
    
    #Test with two non-empty linked lists where the result has more digits than the input lists:
    L1 = LinkedList()
    L1.insert_end(9)
    L1.insert_end(9)
    L1.insert_end(9)
    L2 = LinkedList()
    L2.insert_end(9)
    L2.insert_end(9)
    L2.insert_end(9)
    L3 = AddNums(L1,L2)
    L3.PrintList() # Expected output: None <-> 1  <-> 9  <-> 9  <-> 8  <-> None
    print()

            