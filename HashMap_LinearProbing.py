class Hash_Map:
#Basic Structure
    def __init__(self):
        self.MAX = 10
        self.map = [None for i in range(self.MAX)]
        
    def get_hash(self,key):
    # This is the hash function Fh(x)
        h = 0
        for char in key:
            h += ord(char)
        return h%10
    # %10 since we want the index range to be 0 to 99
#Operational Functions

    def __setitem__(self,key,value):
        index = self.get_hash(key)
        
        if self.map[index] is None:
            self.map[index] = (key,value)
            return
        if index<self.MAX-1:
            x = index +1
        else:
            x = 0
        while(x != index):
            if self.map[x] is None:
                self.map[x] = (key,value)
                return
            if x >= self.MAX:
                x = 0
                continue
            x += 1
        print("Hashmap Overflow!") 
        return
        
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        
        
        if not(self.map[index] is None) and self.map[index][0] == key:
            return self.map[index][1]
        if index<self.MAX-1:
            x = index +1
        else:
            x = 0
        while(x != index):
            if not(self.map[x] is None) and self.map[x][0] == key:
                return self.map[x][1]
            if x >= self.MAX:
                x = 0
                continue
            else:
                x += 1
        return "Key not found!"
    
    def __delitem__(self,key):
        index = self.get_hash(key)
        
        if self.map[index][0] == key:
            self.map[index] = None
            return
        if index<self.MAX-1:
            x = index +1
        else:
            x = 0
        while(x != index):
            if self.map[x][0] == key:
                self.map[x] = None
                return
            if x >= self.MAX:
                x = 0
                continue
            else:
                x += 1
        print("Key not found!")
        return
        
# Same as implementation of Dictionary
# Does not handle collision yet 
    

if __name__ == "__main__":
    Stock_Prices = Hash_Map()
    Stock_Prices['march 6'] = 310
    Stock_Prices['april 7'] = 410
    Stock_Prices['may 8'] = 388
    Stock_Prices['june 10'] = 416
    Stock_Prices['may 2'] = 322 # will cause collision 
    
    print(Stock_Prices.map)
    
    print(Stock_Prices['may 2'])
    print(Stock_Prices['march 6']) # collision handled
    print(Stock_Prices.map)
    
    del Stock_Prices['march 6']
    
    print(Stock_Prices['may 2'])
    print(Stock_Prices['march 6'])
    print(Stock_Prices.map)





