def collapse_tree(tree):
    # If the element is already a string, return it
    if isinstance(tree, str):
        return tree
    
    # If the element is a list, we need to collapse it
    collapsed_list = []
    
    for elem in tree:
        # Recursively collapse each element
        collapsed_list.append(collapse_tree(elem))
    
    # Once all elements of the list are collapsed into strings, concatenate them
    collapsed_string = ''.join(collapsed_list)
    
    return collapsed_string

if __name__ == "__main__":
    input_tree = ["00", ["00", "10110", ["100010", "111001"], "101110"]]
    
    # Collapse the tree into a single string
    output_string = collapse_tree(input_tree)
    
    # Print the final collapsed string
    print(output_string)
