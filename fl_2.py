import sys


def remove_comment(expr_list):
    result = []
    for expr in expr_list:
        if isinstance(expr, list) and isinstance(expr[0], str) and expr[0].startswith('comment'):
            continue
        elif isinstance(expr, list):
            expr = remove_comment(expr)
        result.append(expr)
    return result

code = sys.stdin.read()  
# WARNING!! refactor this 
code = remove_comment(eval(code))
print(code)