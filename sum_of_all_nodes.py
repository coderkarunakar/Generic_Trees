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

def sum_of_nodes(root):
    #base case if root is empty then simply return sum as 0
    if root is None:
        return 0
#initialize total sum with the value of the current root node
    total_sum = root.value
    #iterate through each child of the current root
    for child in root.children:
        #recursively    call sum_of_nodes on each child and add the result to the total sum,this line is calling on each node and adding all those nodes and finally add it to the total sum i.e root value
        total_sum += sum_of_nodes(child)
#return the total sum for the current subtree rooted at root
    return total_sum

# Sample input
root = takeTreeInput()
printTreeDetail(root)

# Calculate and print the sum of all nodes
result = sum_of_nodes(root)
print("the sum of all nodes are",result)
 