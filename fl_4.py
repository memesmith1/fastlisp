
import sys


def replace_lambda(expr_list):
    if isinstance(expr_list, list):
        return [replace_lambda(item) for item in expr_list]
    elif expr_list == 'lambda':
        return '00'
    else:
        return expr_list


expr_list = sys.stdin.read()
expr_list = replace_lambda(eval(expr_list))


print(expr_list)