""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check_binary_search_tree_(root):
    
    def inorder(reference,values):
        if(reference == None):
            return
        inorder(reference.left,values)
        values.append(reference.data)
        inorder(reference.right,values)
    
    values = []
    inorder(root,values)
    
    for i in range(len(values)-1):
        if(values[i] >= values[i+1]):
            return(False)
    return(True)
