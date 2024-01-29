class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree_from_input(input_sequence):
    if not input_sequence:
        return None

    root_value = input_sequence.pop(0)
    root = TreeNode(root_value)

    num_children = input_sequence.pop(0)
    for _ in range(num_children):
        child = build_tree_from_input(input_sequence)
        root.children.append(child)

    return root

def sum_of_nodes(root):
    if root is None:
        return 0

    total_sum = root.value
    for child in root.children:
        total_sum += sum_of_nodes(child)

    return total_sum

# Sample input
input_sequence = [10, 3, 20, 30, 40, 2, 40, 2, 40, 50, 0, 0, 0, 0]

# Build the generic tree
root_node = build_tree_from_input(input_sequence)

# Calculate and print the sum of all nodes
result = sum_of_nodes(root_node)
print(result)
