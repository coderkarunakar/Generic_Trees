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



# Sample input
root = takeTreeInput()
printTreeDetail(root)
x = int(input("please enter the value you are searching"))
print(is_present_in_tree(root, x))  # Output: True

