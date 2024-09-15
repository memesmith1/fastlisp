import sys
import ast

def collapse_tree(tree):
    # Base case: if the element is a string, return it directly
    if isinstance(tree, str):
        return tree
    # Recursive case: if it's a list, concatenate all the collapsed elements within it
    elif isinstance(tree, list):
        collapsed_string = ''.join(collapse_tree(elem) for elem in tree)
        return collapsed_string
    # If it's not a string or list, return it unchanged (unlikely based on input structure)
    else:
        return tree

if __name__ == "__main__":
    # Read input from stdin and parse it as a Python structure
    input_code = sys.stdin.read().strip()
    tree = ast.literal_eval(input_code)  # Safely parse the input string as Python list/tree

    # Collapse the tree into a single string
    result = collapse_tree(tree)

    # Print the final collapsed string to stdout
    print(result)
