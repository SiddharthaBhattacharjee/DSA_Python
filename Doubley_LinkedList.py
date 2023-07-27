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
        op = "None<-->"
        hptr = self.head
        while hptr:
            op = op + str(hptr.data) + "<-->"
            hptr = hptr.next
        op = op + "None"
        print(op)
        return
    
    def insert_at(self,data,pos):
        if pos<0 or pos>self.length():
            print("Invalid Position!")
            return
        c = 0
        hptr = self.head
        if pos == 0:
            self.insert_at_start(data)
        if pos == self.length():
            self.insert_at_end(data)
            return
        while hptr:
            if c+1 == pos:
                x = Node(data,hptr.next,hptr)
                hptr.next = x
                x.next.prev = x
                return
            c+=1
            hptr = hptr.next
            
    def remove_at_start(self):
        self.head = self.head.next
        del self.head.prev
        self.head.prev = None
    
    def remove_at_end(self):
        self.tail = self.tail.prev
        del self.tail.next
        self.tail.next = None
        
    def remove_at(self,pos):
        if pos<0 or pos>=self.length():
            print("Invalid Position !")
            return
        if pos == 0:
            self.remove_at_start()
            return
        if pos == self.length() - 1:
            self.remove_at_end()
            return
        c = 0
        ptr = self.head
        while ptr:
            if c+1 == pos:
                ptr.next = ptr.next.next
                del ptr.next.prev
                ptr.next.prev = ptr
                return
            c += 1
            ptr = ptr.next
            
    def search(self,item):
        ptr = self.head
        c=0
        while ptr:
            if ptr.data == item:
                return c
            ptr = ptr.next
            c += 1
        return -1
        
    
if __name__ == "__main__":
    ll = DoubleyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(30)
    ll.insert_at_end(40)
    ll.insert_at(50,4)
    ll.print_list()
    print(ll.length())
    ll.remove_at(3)
    ll.print_list()
    print(ll.length())
    print(ll.search(20))