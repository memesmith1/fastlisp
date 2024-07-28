import sys
import re

def convertStringToArrayOfTrueAndFalse(s):
    boolean_array = []
    for char in s:
        code_point = ord(char)
        binary_representation = bin(code_point)[2:]  # remove the '0b' prefix
        binary_representation = binary_representation.zfill(8)
        boolean_array.extend([bit == '1' for bit in binary_representation])
    return boolean_array

def convertArrayOfTrueAndFalseToVierosOfKestrelAndKite(boolean_array):
    result = []
    for bit in boolean_array:
        if bit:
            result.append("(viero kestrel ")
        else:
            result.append("(viero kite ")
    result.append(")" * len(boolean_array))
    return ''.join(result)

def convertStringToVierosOfKestrelAndKite(s):
    boolean_array = convertStringToArrayOfTrueAndFalse(s)
    return convertArrayOfTrueAndFalseToVierosOfKestrelAndKite(boolean_array)

def main():
    input_data = sys.stdin.read()
    
    def remove_comments(text):
        pattern = re.compile(r'\(comment.*?\)', re.DOTALL)
        while re.search(pattern, text):
            text = re.sub(pattern, '', text)
        return text

    def replace_text_blocks(text):
        pattern = re.compile(r'\(text(.*?)\)', re.DOTALL)
        def replace_match(match):
            content = match.group(1).strip()
            content = content.replace('\\', '\\\\').replace('"', '\\"')
            viero_string = convertStringToVierosOfKestrelAndKite(content)
            return viero_string
        return re.sub(pattern, replace_match, text)

    def ensure_spaces_around_parentheses(text):
        text = re.sub(r'\s*\(\s*', ' ( ', text)
        text = re.sub(r'\s*\)\s*', ' ) ', text)
        return text

    def assign_unique_names(text):
        ignore_symbols = {')', '(', 'lambda', 'viero', 'kestrel', 'kite'}
        unique_counter = 1
        symbol_mapping = {}
        
        def replace_symbol(match):
            symbol = match.group(0)
            if symbol in ignore_symbols:
                return symbol
            if symbol not in symbol_mapping:
                nonlocal unique_counter
                unique_name = f"unique_name_{unique_counter}"
                symbol_mapping[symbol] = unique_name
                unique_counter += 1
            return symbol_mapping[symbol]

        # Regex to match symbols (alphanumeric strings)
        symbol_pattern = re.compile(r'\b\w+\b')
        return re.sub(symbol_pattern, replace_symbol, text)

    modified_data = remove_comments(input_data)
    modified_data = replace_text_blocks(modified_data)
    modified_data = modified_data.replace('\n', ' ')
    modified_data = re.sub(r'\s+', ' ', modified_data)
    modified_data = ensure_spaces_around_parentheses(modified_data)
    modified_data = assign_unique_names(modified_data)

    print(modified_data.strip(), end='')

if __name__ == "__main__":
    main()
