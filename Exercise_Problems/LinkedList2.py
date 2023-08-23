"""__ProblemStatement__:
        Write a function to reverse a linked list
"""

class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val,None)
            return
        newnode = Node(val,self.head)
        self.head = newnode
        
    def append(self,val):
        if self.head is None:
            self.head = Node(val,None)
            return
        ptr = self.head
        while(ptr.next):
            ptr = ptr.next
        ptr.next = Node(val,None)
    
    def Print(self):
        if self.head is None:
            print("Empty Linked List!")
            return
        ptr = self.head
        while(ptr):
            print(ptr.val,end="->")
            ptr = ptr.next
        print("None")
        
    def Reverse(self):
        stack = []
        ptr = self.head
        while(ptr):
            stack.insert(0,ptr.val)
            ptr = ptr.next
        temp = LinkedList()
        for x in stack:
            temp.append(x)
        self.head = temp.head
        
if __name__ == "__main__":
    LL = LinkedList()
    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.Print()
    LL.Reverse()
    LL.Print()