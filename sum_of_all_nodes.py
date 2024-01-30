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
def find_largest_node(root):
    #base case
    if not root:
        return None

    # Initialize max_data with the value of the root node,initially
    max_data = root.value

    # Iterate through children and recursively find the maximum value
    for child in root.children:
        child_max = find_largest_node(child)
        #child max is greater than the root value i.e max_data then simply replace it ,and max_data get updated regularly and stores it in the max_data and finally returns it
        if child_max is not None and child_max > max_data:
            max_data = child_max

    return max_data


def find_tree_height(root):
    #base case if there is no root then simply return height as 0
    if not root:
        return 0

    # Calculate the height of each child and find the maximum
    #initially keeping max child height as 0 
    max_child_height = 0
    #iterating into the root's children 
    for child in root.children:
        #calling the function recursively 
        child_height = find_tree_height(child)
        #picking the max height among the our initialized one and height of the child height in the root's children
        max_child_height = max(max_child_height, child_height)

    # Add 1 to the maximum child height to account for the current level
    return 1 + max_child_height

# Sample input
root = takeTreeInput()
printTreeDetail(root)

# Calculate and print the sum of all nodes
result = sum_of_nodes(root)
print("the sum of all nodes are",result)
 # Find the node with the largest data
largest_node_data = find_largest_node(root)

# Print the result
print(largest_node_data)


height = find_tree_height(root)
print("Height of the tree:", height)