import sys
import ast

def transform_list(lst):
    # Check if the list starts with "00"
    if lst[0] == "00":
        # Only insert "01" if there are multiple items after "00"
        if len(lst) > 2:
            prepend = ["01"] * (len(lst) - 2)  # Add "01" for each item after the first one
            return [lst[0]] + prepend + lst[1:]
        else:
            return lst  # No "01" added if only one item follows "00"
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
