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
    ll.insert_at_start(10)
    ll.insert_at_start(20)
    ll.insert_at_start(30)
    ll.Print_List()