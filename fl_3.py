import sys

def convert_to_de_bruijn(expr_list, depth=0, context=None):
    if context is None:
        context = []

    if not isinstance(expr_list, list):
        if expr_list in context:
            return context.index(expr_list)
        return expr_list

    result = []
    i = 0
    while i < len(expr_list):
        if expr_list[i] == 'lambda':
            result.append('lambda')
            i += 1
            if i < len(expr_list) and isinstance(expr_list[i], str):
                context = [expr_list[i]] + context
                result.append(depth)
                i += 1
            if i < len(expr_list):
                result.append(convert_to_de_bruijn(expr_list[i], depth + 1, context))
        else:
            if isinstance(expr_list[i], str) and expr_list[i] in context:
                result.append(context.index(expr_list[i]))
            else:
                result.append(convert_to_de_bruijn(expr_list[i], depth, context))
        i += 1

    return result

# Example usage

expr_list = sys.stdin.read()

# WARNING!! refactor this 'eval'
converted_expr_list = convert_to_de_bruijn(eval(expr_list))
print(converted_expr_list)
