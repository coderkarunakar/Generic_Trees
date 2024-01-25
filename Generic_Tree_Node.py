#Creating a Generic Tree Node
class TreeNode:
    def __init__(self,data):
        self.data = data
        #creating an empty list
        self.children = list()
def printTree(root):
    #this is not a base case it is a edge case ,if someone gives none then it is going to be crashed,here our base case is a leaf ,if we reach leaf then it is going to be stopped
    if root == None:
        return 
        #first root data
    print(root.data)
    #prints using depth first traversal
    for child in root.children:
        printTree(child)

def printTreeDetail(root):
    #edge case
    if root == None:
        return
        #this will print roots value first ,and i dont want to print on new line so using end= ""
    print(root.data, ":" ,end="")
    #for below call this will print 
            #this will call on each child ,root.children is a way to access and iterate through the immediatechilren of node in the tree structure
            #this is for printing the children
            #e line paina print ina root lo child emain unte dan data ni print chestunde
    for child in root.children:
        print(child.data, ",", end="")
    #this to get a new line 
    print() 
#this is for calling the children 
#paina print chesina 1st danni oka child ki malli malli call chestundi
    for child in root.children:
        #by calling the above function,by pasing child index to check its children
        printTreeDetail(child)

n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(7)
n6 = TreeNode(15)
n7 = TreeNode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)
n3.children.append(n6)
n3.children.append(n7)

# printTree(n1)
printTreeDetail(n1)