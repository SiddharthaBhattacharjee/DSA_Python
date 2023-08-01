class Hash_Map:
#Basic Structure
    def __init__(self):
        self.MAX = 100
        self.map = [None for i in range(self.MAX)]
        
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
        self.map[index] = value
        return
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        return self.map[index]
    
    def __delitem__(self,key):
        index = self.get_hash(key)
        self.map[index] = None
        
# Same as implementation of Dictionary
# Does not handle collision yet 
    

if __name__ == "__main__":
    Stock_Prices = Hash_Map()
    Stock_Prices['march 6'] = 310
    Stock_Prices['april 7'] = 410
    Stock_Prices['may 8'] = 388
    Stock_Prices['june 10'] = 416
    Stock_Prices['may 2'] = 322 # will cause collision 
    
    print(Stock_Prices['april 7'])
    print(Stock_Prices['march 6']) # collision detected
    
    del Stock_Prices['april 7']
    
    print(Stock_Prices['april 7'])



