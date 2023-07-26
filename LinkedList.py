class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_start(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        hptr = self.head
        while hptr:
            if hptr.next is None:
                hptr.next = Node(data,None)
                break
            hptr = hptr.next
        
    def Print_List(self):
        hptr = self.head
        Lstr = ""
        
        if hptr is None:
            print("Empty LinkedList!")
            pass
        
        while hptr:
            Lstr += str(hptr.data) + "-->"
            hptr = hptr.next
        Lstr += 'None'
        print(Lstr)
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.Print_List()