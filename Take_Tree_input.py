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

def takeTreeInput():
    print("Enter the root data")
    rootData = int(input(""))
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    #for every single node this will be processed
    print("Enter the no of children for", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        #for that particular child it is calling again the above function
        child = takeTreeInput()
        root.children.append(child)
    return root
def numNodes(root):
    if root == None:
        return 0
    count =1 
    for child in root.children:
        #increments the count by recursively calling the numnodes   function on each child of the current node,effectively counting all nodes in the subtree rooted at the current node
        count = count + numNodes(child)
    return count
root = takeTreeInput()
printTreeDetail(root)
print("the no of nodes is ",numNodes(root))