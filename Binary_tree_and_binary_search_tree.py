#to day topic 
#TREE
#IT IS THE nnon linear data sterctuer.



# INTRODUCTION TO TEH TREE DATA STRUCTURE
    #   A  tree is a nonlinear hierarchical data 
    # structuer the consists of the nodes connected by edges.
#TREE TERMIMOLOGIES

#Node-A node is an entity contains a key or value and pointers to its child
 
#the last nodes of each path are called leaf nodes or external nodes that do not
# contain a link between any two nodes.

#Edge- it is the link between any two nodes

#Root- it is the topmost of a tree.

#Degree of a node - the degree of a node is the total number of branches 
# of the node.

#Height and Depthe of tree

#PROPERTIS OF THE TREE

# thire shoul no any cycle in the tree
# it shoul be the connected with each other
#  if n node ___---- (n-1)edges
#  tree is the directed(each edges as the direction)


#             Binary tree

# a binary tree is a tree data structure in which each parent node can have 
#  at most two children . each node of a binary tree itemss :(one node as at most two or less childs)

#   . data item
#   . address of left child 
#   . address of right child

# 

class Node:
    def __init__(self,data):
        self.data=data
        self.right=Node
        self.left=Node
root=Node(5)        
root.right=Node(3)
root.left=Node(1)
root.left.right=Node(8)

print(root.right.data)
print(root.left.right.data)