#Node , individual cell of the LinkedList
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
#LinkedList Class
class LinkedList:
    #Constructor , no parameter at instanciation
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
            # while hptr.next:
            #     if hptr.next is None:
            #         hptr.next = Node(data,None)
            #         break
            #     hptr = hptr.next
            #SlightLy Improved
        while hptr.next:
            hptr = hptr.next
        hptr.next = Node(data,None)
        
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
        
    def Initialize_List(self, datas):
        self.head = None
        for i in datas:
            self.insert_at_end(i)
            
    def length(self):
        len = 0
        hptr = self.head
        while hptr:
            len += 1
            hptr = hptr.next
        return len
    
    def remove_start(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def remove_end(self):
        hptr = self.head
        while(hptr.next.next):
            hptr = hptr.next
        hptr.next = None
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.Initialize_List([10,20,30,40,50])
    ll.Print_List()
    print(ll.length())
    ll.remove_start()
    ll.Print_List()
    print(ll.length())