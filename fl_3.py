import sys

def convert_to_de_bruijn(expr_list, depth=0, context=None):
    if context is None:
        context = []

    if not isinstance(expr_list, list):
        # If the element is in the context, return its index
        if expr_list in context:
            return context.index(expr_list)
        return expr_list

    result = []
    i = 0
    while i < len(expr_list):
        if expr_list[i] == 'lambda':
            result.append('lambda')
            i += 1
            # Skip the next element (the bound variable), but add it to the context
            if i < len(expr_list) and isinstance(expr_list[i], str):
                context = [expr_list[i]] + context
                i += 1  # Skip the bound variable
            # Recurse into the body of the lambda
            if i < len(expr_list):
                result.append(convert_to_de_bruijn(expr_list[i], depth + 1, context))
        else:
            # For non-lambda elements, check if they are in the context
            if isinstance(expr_list[i], str) and expr_list[i] in context:
                result.append(context.index(expr_list[i]))
            else:
                result.append(convert_to_de_bruijn(expr_list[i], depth, context))
        i += 1

    return result

if __name__ == "__main__":
    # Read the input from stdin
    expr_list = sys.stdin.read().strip()

    # WARNING!! Refactor this 'eval' for safer input handling in production
    parsed_expr_list = eval(expr_list)

    # Convert the expression list to De Bruijn form
    converted_expr_list = convert_to_de_bruijn(parsed_expr_list)

    # Output the converted list
    print(converted_expr_list)
