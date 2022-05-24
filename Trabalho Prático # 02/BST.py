# Author: Luiz Thadeu Grizendi
# UniAcademia, Juiz de Fora MG - Brasil

from BSTNode import BSTNode
from BinaryTree import binaryTree
 
# BST_Tree class  
class BST(binaryTree):
    def __init__(self,items=None):
        super().__init__()
        if items:
            entries=[]
            if(type(items) is list):
                entries=items
            elif(type(items) is dict):
                entries=items.items()
            elif(type(items).__name__ ==  type(self).__name__):
                entries=items.items()
            else:
                raise TypeError("'"+type(items).__name__+"'"+' object is not iterable')
            for k,v in entries:
                self.put(k,v)
        
    def __iter__(self):
        return iter(self.items())

    def __eq__(self,other):
        if type(self) == type(other): 
            return self.items() == other.items()
        return False

    def __ne__(self,other):
        return not self == other

    def __add__(self,other):
        t = self.copy()
        t.extend(other.items())
        return t

    def __sub__(self,other):
        t = self.copy()
        for k in other.keys():
            #print(k)
            if k in t:
                #print(k)
                t.remove(k)
        return t

    def __contains__(self,key):
        if isinstance(key,tuple):
            return self.find(key[0])and key == (key[0],self.get(key[0]))
        return self.find(key)

    def contains(self,key):
        return key in self

    def __getitem__(self, key): 
       if (type(key) is slice):
            raise TypeError("unhashable type: 'slice'")
       if key in self:
           return self.get(key)
       raise KeyError(key)
         
    def __delitem__(self, key):
        if not key in self:
            raise TypeError(key)
        return self.remove(key)      

    def __setitem__(self, key,value):
        self.put(key,value)
    
    def __str__(self):
        return str(dict(self))
     
    def __dict__(self): 
        return dict(self.items())

    # function to insert key, value in BST  
    def put(self,key,value):
        self._size += 1
        self._root=self._insert(self._root,key,value)
        
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def _insert(self, root, key,value):
         
        # Step 1 - Perform normal BST 
        if root==None: 
            return BSTNode(key,value) 
        elif key < root.key: 
            root.left = self._insert(root.left, key,value) 
        elif key > root.key: 
            root.right = self._insert(root.right, key,value)
        else:
            self._size -= 1        
            # key equal, replace value
            root.value = value
        return root 

    def pop(self,key):
        return self.remove(key)    
    
    # Recursive function to delete a node with 
    # given key from subtree with given root. 
    # It returns root of the modified subtree. 
    def _delete(self, root, key): 
        # Step 1 - Perform normal BST   
        if not root: 
            return root 
        elif key < root.key: 
            root.left = self._delete(root.left, key)  
        elif key > root.key: 
            root.right = self._delete(root.right, key) 
        else: 
            # cases 1 or 2 : node is leaf or has one child
            if root.left is None: 
                temp = root.right 
                root = None
                return temp   
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            # caso 3 - node with two children
            temp = self._successor(root.right) 
            root.key = temp.key
            root.val = temp.value 
            root.right = self._delete(root.right, 
                                      temp.key)
        return root

    def _rec_get(self,root,key):
        if root==None:
            return root
        if key < root.key:
            return self._rec_get(root.left, key) 
        elif key > root.key: 
            return self._rec_get(root.right, key) 
        else: 
            return root.value
    
    def get(self, key): 
        return self._rec_get(self._root,key)
        
    def find(self,key):
        return not self.get(key) == None     
        
    def keys(self):
        return [key for key,value in self.items()]

    def values(self):
        return [value for key,value in self.items()]
        
    def entries(self):
        return self.items()
    
    def items(self):
        return self.inOrder()
                
    def copy(self):
        return BST(self.items())

    def update(self,iterable):
        return self.extend(iterable)
    
    def extend(self,iterable):
        entries=[]
        if type(iterable) is dict:
            entries=iterable.items()    
        elif type(iterable).__name__ == type(self).__name__:
            entries=iterable.items()    
        elif type(iterable) is list:
            if not type(iterable[0]) is tuple:
                raise TypeError('TypeError: cannot convert '+type(self).__name__+' update sequence element #0 to a sequence')
            entries=iterable    
        else:
            raise TypeError('TypeError: cannot convert '+type(self).__name__+' update sequence element #0 to a sequence')
        for k,v in entries:
            self.put(k,v)

    def insertLeft(self,entry='This method is not implemented in the subclass'):
        print('This method is not implemented in the subclass')
        pass

    def insertRight(self,entry='This method is not implemented in the subclass'):
        print('This method is not implemented in the subclass')
        pass
    
if __name__ == '__main__':
    t = BST()
    t.put(20,'ana')
    t.put(30,'bia')
    t.put(10,'leila')
    t.put(25,'maria')
    
