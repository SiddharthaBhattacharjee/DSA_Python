class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoubleyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_start(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            self.tail = self.head
            return
        self.head.prev = Node(data,self.head,None)
        self.head = self.head.prev
        return
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            self.tail = self.head
            return
        self.tail.next = Node(data,None,self.tail)
        self.tail = self.tail.next
        return
    
    def length(self):
        c = 0
        hptr = self.head
        while hptr:
            c += 1
            hptr = hptr.next
        return c
    
    def print_list(self):
        if self.head is None:
            print("Empty Double Linked List!")
            return
        op = ""
        hptr = self.head
        while hptr:
            op = op + str(hptr.data) + "<-->"
            hptr = hptr.next
        op = op + "None"
        print(op)
        return
    
if __name__ == "__main__":
    ll = DoubleyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(30)
    ll.print_list()
    print(ll.length())