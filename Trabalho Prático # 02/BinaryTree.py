# Author: Luiz Thadeu Grizendi
# UniAcademia, Juiz de Fora MG - Brasil

from BinaryTreeNode import binaryTreeNode
import sys

class binaryTree(object):
    def __init__(self):
        self._root = None
        self._size = 0
        
    def __iter__(self):
        return iter(self.inOrder())

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self.inOrder())

    def __repr__(self):
        return type(self).__name__+"-> "+str(self)

    def __contains__(self,element):
        return element in self.inOrder()

    def preOrder(self):
         tr = []
         def bodyPreOrder(root):
             if root:
                 tr.append(root.get_element())
                 bodyPreOrder(root.left)
                 bodyPreOrder(root.right)
             return tr
   
         return bodyPreOrder(self._root)
          
    def posOrder(self):
         tr = []
         def bodyPosOrder(root):
             if root:
                 bodyPosOrder(root.left)
                 bodyPosOrder(root.right)
                 tr.append(root.get_element())
             return tr

         return bodyPosOrder(self._root)
     
    def inOrder(self):
         tr = []
         def bodyInOrder(root):
             if root:
                 bodyInOrder(root.left)
                 tr.append(root.get_element())
                 bodyInOrder(root.right)          
             return tr

         return bodyInOrder(self._root)

         
    def insertLeft(self,currNode,element):     
        if currNode == None: # insert root
            self._root = binaryTreeNode(element) 
        else:
            currNode.left = binaryTreeNode(element)
        self._size += 1
        
    def insertRight(self,currNode,element):     
        if currNode == None: # insert root
            self._root = binaryTreeNode(element) 
        else:
            currNode.right = binaryTreeNode(element)
        self._size += 1

    
    # Recursive function to delete a node with 
    # given element from subtree with given root. 
    # It returns root of the modified subtree. 
    def _delete(self, root, element): 
        # Step 1 - Perform normal Binary Tree   
        if not root: 
            return root 
        elif element != root.element: 
            root.left = self._delete(root.left, element)
            root.right = self._delete(root.right, element) 
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
            root.element = temp.element
            root.right = self._delete(root.right, 
                                      temp.element) 
        return root

        # If the tree has only one node, 
        # simply return it 
        #if root is None: 
        #    return root   
        #return root

   # Recusive function return-> predecessor node
    def _predecessor(self,node): 
        if(node.right != None ):
            return self._predecessor(node.right)
        return node

    # Recusive function return-> successor node    
    def _successor(self,node): 
        if(node.left != None ):
            return self._successor(node.left)
        return node
    
    def isEmpty(self):
        return self._root == None

    def show(self):
        # adapted from https://www.worldofitech.com/red-black-tree-insertion/
        self._show(self._root, "", True)

    # Printing the tree
    def _show(self, node, indent, last):
        # adapted from https://www.worldofitech.com/red-black-tree-insertion/
        if node != None:
            sys.stdout.write(indent)
            if last:
                if node == self._root:
                    sys.stdout.write("Root.")
                else:    
                    sys.stdout.write("R....")
                indent += "     "
            else:
                sys.stdout.write("L....")
                indent += "|    "
            print(str(node.get_element()))
            self._show(node.left, indent, False)
            self._show(node.right, indent, True)

    def clear(self):
        self.__init__()

    def size(self):
        return len(self)
        
if __name__ == '__main__':
    
    t = binaryTree()    
    t.insertLeft(t._root,20)
    t.insertRight(t._root,30)
    t.insertLeft(t._root,10)
    t.insertLeft(t._root.right,25)


    
