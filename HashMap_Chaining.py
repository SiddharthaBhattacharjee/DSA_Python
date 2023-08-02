class Hash_Map:
#Basic Structure
    def __init__(self):
        self.MAX = 100
        self.map = [[] for i in range(self.MAX)]# 2D array -> Map:[[list1][list2]....[list100]]
        
    def get_hash(self,key):
    # This is the hash function Fh(x)
        h = 0
        for char in key:
            h += ord(char)
        return h%100
    # %10 since we want the index range to be 0 to 99
#Operational Functions

    def __setitem__(self,key,value):
        index = self.get_hash(key)
        
        for inx, element in enumerate(self.map[index]):
            if len(element) == 2 and element[0] == key:
                self.map[index][inx] = (key,value)
                return
        self.map[index].append((key,value))
        return
        
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        
        if not self.map[index][0]:
            return None
        
        for element in self.map[index]:
            if element[0] == key:
                return element[1]
        return None
    
    def __delitem__(self,key):
        index = self.get_hash(key)
        
        for inx, element in enumerate(self.map[index]):
            if len(element) == 2 and element[0] == key:
                self.map[index].pop(inx)
                return
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
    
    print(Stock_Prices['may 2'])
    print(Stock_Prices['march 6']) # collision handled
    print(Stock_Prices.map)
    
    del Stock_Prices['march 6']
    
    print(Stock_Prices['may 2'])
    print(Stock_Prices['march 6'])
    print(Stock_Prices.map)





