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
    def add(self,key,value):
        index = self.get_hash(key)
        self.map[index] = value
        return
    
    def get(self,key):
        index = self.get_hash(key)
        return self.map[index]
    
    def delete(self,key):
        self.map[key] = None      
    

if __name__ == "__main__":
    Stock_Prices = Hash_Map()
    Stock_Prices.add('march 6',310)
    Stock_Prices.add('april 7',401)
    Stock_Prices.add('may 8',388)
    Stock_Prices.add('june 10',416)
    
    print(Stock_Prices.get('april 7'))
    



