class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def printTree(root):
    if root is None:
        return
    print(root.value)
    for child in root.children:
        printTree(child)

def printTreeDetail(root):
    if root is None:
        return
    print(root.value, ":", end="")
    for child in root.children:
        print(child.value, ",", end="")
    print()
    for child in root.children:
        printTreeDetail(child)

def takeTreeInput():
    print("Enter the root data")
    rootData = int(input(""))
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("Enter the no of children for", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

#is x present in the tree or not
def is_present_in_tree(root, x):
    #check if the current root node is none base case
    if not root:
        return False
#check if the value of the current node is x ,if yes then simply return true
    if root.value == x:
        return True
#iterate through each child of the current node
    for child in root.children:
        #it is a recursive call,there for every index it is checking true or not ,if true ,there i.e above condition root.value == x ,if true then here it simply returns true not checking for other conditons ,if not true checks untill iteration get completed ,even though it is not true then it returns false
        if is_present_in_tree(child, x):
            return True
#if  x is not found in the current node or its children then simply return false
    return False

#Nodes greater than y
def count_nodes_greater_than_y(root, x):
    if root is None:
        return 0

    count = 0

    # Iterate through children
    #this part iterates through each child of the current root node,in treenode class each node has a list of children and this loop going through each child in that list
    #NOTE:this is checking only for root.children 
    for child in root.children:
        # for each child in that loop it makes a recursive call to this function,this call is essential for traveling the tree structure
        # Count the nodes with values greater than x in the subtree rooted at the current child, and add that count to the total count,with this also count value is getting increased overall
        count += count_nodes_greater_than_y(child, x)
#NOTE:this is checking for the main root value
    # Check the current node,this is for that main root value,with this the count value is getting increase by 1 because of checking the root value
    if root.value > x:
        count += 1

    return count
#please look in class notes for dry run it is simple one

# Sample input
root = takeTreeInput()
printTreeDetail(root)
x = int(input("please enter the value you are searching"))
print(is_present_in_tree(root, x))  # Output: True

y = int(input("please enter value of y in order to get values greater than y"))
# Find and print the number of nodes with data greater than x
result = count_nodes_greater_than_y(root, y)
print("Number of nodes with data greater than", y, "is:", result)