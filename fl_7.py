import sys
import ast

def transform_list(lst):
    # If the list starts with the string "00", return it unchanged
    if lst[0] == "00":
        return lst
    else:
        # Prepend "01" (len(lst) - 1) times to the list
        prepend = ["01"] * (len(lst) - 1)
        return prepend + lst

def transform_tree(tree):
    result = []
    for elem in tree:
        if isinstance(elem, list):
            # If the element is a list, recursively transform it
            result.append(transform_tree(elem))
        else:
            # If the element is not a list, just append it (as per given structure)
            result.append(elem)
    return transform_list(result)

if __name__ == "__main__":
    # Read input from stdin and parse it as a Python list
    input_code = sys.stdin.read()
    tree = ast.literal_eval(input_code)  # Safely parse the input string as Python structure

    # Transform the input tree
    output_code = transform_tree(tree)

    # Print the transformed output to stdout
    print(output_code)

