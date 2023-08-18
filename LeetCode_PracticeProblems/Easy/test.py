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
            print("")
            pass
        
        while hptr:
            Lstr += str(hptr.data)
            if hptr.next:
                Lstr = Lstr+"->"
            hptr = hptr.next
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
        t = self.head.next
        del self.head
        self.head = t
        
    def remove_end(self):
        hptr = self.head
        while(hptr.next.next):
            hptr = hptr.next
        del hptr.next
        hptr.next = None
        
    def remove_at(self,pos):
        if pos<0 and pos>=self.length():
            return
        elif pos==0:
            self.remove_start()
            return
        c = 0
        hptr = self.head
        while hptr.next:
            if c==pos-1:
                x = hptr.next.next
                del hptr.next
                hptr.next = x
                return
            hptr = hptr.next
            c += 1
            
        
    def Insert_at(self,data,pos):
        if pos<0 and pos>self.length():
            return
        elif pos==0:
            self.insert_at_start(data)
            return
        c = 0
        hptr = self.head
        while hptr:
            if c==pos-1:
                hptr.next = Node(data,hptr.next)
                return
            hptr = hptr.next
            c += 1
    
    def insert_after_value(self,data,val):
        hptr = self.head
        while hptr:
            if hptr.data == val:
                hptr.next = Node(data,hptr.next)
                return
            hptr = hptr.next
        print("Value not found!")    
    
    def remove_by_value(self,val):
        hptr = self.head
        if hptr.data == val:
            self.remove_start()
            return
        while hptr:
            if hptr.next and hptr.next.data == val:
                x = hptr.next.next
                del hptr.next
                hptr.next = x
                return
            hptr = hptr.next      
        
if __name__ == "__main__":
    ll = LinkedList()
    l = int(input())
    