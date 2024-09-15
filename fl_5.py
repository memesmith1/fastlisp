import sys

def convert_to_binary(expr_list):
    if isinstance(expr_list, int):
        return bin(expr_list)[2:]
    elif isinstance(expr_list, list):
        return [convert_to_binary(item) for item in expr_list]
    else:
        return expr_list

expr_list = sys.stdin.read()
# WARNING: refactor 'eval' its not good
print(convert_to_binary(eval(expr_list)))
