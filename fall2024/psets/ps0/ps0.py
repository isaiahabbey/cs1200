#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v is None:
        return 0
    left_size = calculate_sizes(v.left)
    right_size = calculate_sizes(v.right)

    v.size = 1 + left_size + right_size
    return v.size 
    pass 

#The operating time is O(n) because the program runs through every vertex to find the subtrees, so it has a linear relation to the number of nodes


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    if v is None:
        return 0
    #this will return the node that has a subtree with a size within these constraints
    if t <= v.size <= 2*t:
        return v
    if v.size >= t and v.left.size is not None:
        return FindDescendantOfSize(t,v.left)
    if v.size < t and v.right.size is not None:
        return FindDescendantOfSize(t,v.right)
    return None
    pass 
    
#since h is the height of the subtree rooted at v, the program needs to search all nodes to find a descendant with thr desired subtree size. so depending how many generations there are (the height) determines how many nodes will be searched
