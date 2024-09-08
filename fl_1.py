import re
import sys

def convert_parentheses_to_list(code):
    def helper(code, index):
        result = []
        while index < len(code):
            if code[index] == '(':
                sublist, index = helper(code, index + 1)
                result.append(sublist)
            elif code[index] == ')':
                return result, index + 1
            else:
                match = re.match(r'\s*([^()\s]+)\s*', code[index:])
                if match:
                    result.append(match.group(1))
                    index += len(match.group(0))
                else:
                    index += 1
        return result, index

    return helper(code, 0)[0]

def main():
    code = sys.stdin.read()  

    result = convert_parentheses_to_list(code)
    print(result)

if __name__ == "__main__":
    main()