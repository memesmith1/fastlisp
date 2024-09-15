import sys

def convert_to_unary(expr_list):
    if isinstance(expr_list, int):
        # Convert integer to unary (a series of 1's followed by a 0)
        return '1' * expr_list + '0'
    elif isinstance(expr_list, list):
        # Recursively convert each item in the list
        return [convert_to_unary(item) for item in expr_list]
    else:
        return expr_list

if __name__ == "__main__":
    expr_list = sys.stdin.read()
    # WARNING: refactor 'eval' as it may be unsafe for untrusted input
    parsed_list = eval(expr_list)  # Parse the input string to a Python list or int

    # Convert the parsed list or int to unary representation
    result = convert_to_unary(parsed_list)

    # Print the result
    print(result)
