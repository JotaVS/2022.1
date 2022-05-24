class binaryTreeNode:
     def __init__(self,element):
        self.element = element
        self.left = None
        self.right = None

     def __str__(self):
          return str(self.element)

     def __repr__(self):
          return repr(self.element)

     def get_element(self):
          return self.element
