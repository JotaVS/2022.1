# Generic BSTNode class 
class BSTNode(): 
    def __init__(self, key,value):
        self.key = key
        self.value = value 
        self.left = None 
        self.right = None 

    def get_element(self):
        return (self.key,self.value)
    
    def __str__(self):
          return str((self.key,self.value))

    def __repr__(self):
          return str(self)
