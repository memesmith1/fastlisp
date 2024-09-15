import sys

def intersperse_ones(binary_number):
    modified_number = ""
    for bit in binary_number:
        modified_number += "1" + bit
    modified_number = modified_number[:-1] + "0"
    return modified_number

def apply_function(tree, func):
    if isinstance(tree, str):
        if tree != '00':
            return func(tree)
        else:
            return tree
    elif isinstance(tree, list):
        return [apply_function(subtree, func) for subtree in tree]
    else:
        return tree

expr_list = sys.stdin.read()
tree = eval(expr_list)  # Convert the input string to a nested list
modified_tree = apply_function(tree, intersperse_ones)  # Replace strings using your_function

# Print the modified tree
print(modified_tree)
