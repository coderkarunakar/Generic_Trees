#Tree input Level wise
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

    count = 1
    for  child in root.children:
        count = count + numNodes(child)
    return count


import queue

def takeTreeInputLevelWise():
    q = queue.Queue()
#here you are suppose to enter the root value,with this root data is created
    print("Enter root")
    rootData = int(input())
#     #we are not doing recursively ,we are doing it iteratively ,so below one is  a edge case ,it is not a base case
    
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
#     #while the queue is not empty we will be doing some work,take out the first element from the queue,find out its children,iterate those many of children,and get that child data,using that create a childnode and connect it wiht the current node i have ,append it to children node,now put this child inside the queue,finally return root

    while not q.empty():
        current_node = q.get()
        
        #current_node is getting  changed... take a look on dry run but easy 
        print("Enter num of children for", current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for", current_node.data)
            childData = int(input())
            
            child = TreeNode(childData)
            #because of this only we are able to get the child as current node and get its child first
            current_node.children.append(child)
            q.put(child)

    return root

root = takeTreeInputLevelWise()
printTreeDetail(root)
print(numNodes(root))
