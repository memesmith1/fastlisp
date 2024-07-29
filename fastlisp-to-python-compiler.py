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
        ignore_symbols = {'(', ')', 'lambda', ':'}
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

        # Treat everything between spaces as symbols, including handling special cases
        symbol_pattern = re.compile(r'\S+')
        return re.sub(symbol_pattern, replace_symbol, text)

    def wrap_symbols(text):
        ignore_symbols = {'(', ')', 'lambda', ':'}
        
        def wrap_symbol(match):
            symbol = match.group(0)
            if symbol in ignore_symbols:
                return symbol
            return f"( {symbol} )"
        
        symbol_pattern = re.compile(r'\S+')
        return re.sub(symbol_pattern, wrap_symbol, text)

    def unwrap_symbols_after_lambda(text):
        # Pattern to match "lambda ( symbol )"
        pattern = re.compile(r'(lambda)\s*\(\s*(\S+)\s*\)')
        return re.sub(pattern, r'\1 \2', text)

    def insert_colon_after_lambda(text):
        # Pattern to match "lambda symbol" and add colon after symbol
        pattern = re.compile(r'(lambda\s+\S+)')
        return re.sub(pattern, r'\1 :', text)

    #1.remove comments
    #2. replace text with vieros of kestral and kite
    #3. change all newline characters to space
    #4. for all instnaces of repeated spaces change it to one space
    #5. make sure there is exactly one space inbetween every symbol
    #6. for each instance of a new symbol give it a unique name unless it is (, ), kestrel, kite, viero, lambda, or :
    #7. for all symbols except (, ), kestrel, kite, viero, lambda, and : wrap it in parentheses
    #8. if a symbol comes directly after lambda remove the parentehses
    #9. for the symbol that comes directly after lambda insert " : " after it

    modified_data = remove_comments(input_data)
    modified_data = replace_text_blocks(modified_data)
    modified_data = modified_data.replace('\n', ' ')
    modified_data = re.sub(r'\s+', ' ', modified_data)
    modified_data = ensure_spaces_around_parentheses(modified_data)
    modified_data = assign_unique_names(modified_data)
    modified_data = wrap_symbols(modified_data)
    modified_data = unwrap_symbols_after_lambda(modified_data)
    modified_data = insert_colon_after_lambda(modified_data)

    print(modified_data.strip(), end='')

if __name__ == "__main__":
    main()
