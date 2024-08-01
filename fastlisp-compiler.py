import sys

def main():

    debugging_enabled=0
    def debug(x):
        if debugging_enabled:
            print(x)

    # Read input from stdin
    input_code = sys.stdin.read().strip()

    
    abstract_syntax_tree=[[]]
    
    abstract_syntax_tree_stack=[abstract_syntax_tree]

    abstract_syntax_tree_current_string=""

    parsing_backslash = 0
    for current_character in input_code:
        debug("current character is")
        debug(current_character)
        if parsing_backslash:
            abstract_syntax_tree_current_string = abstract_syntax_tree_current_string + current_character
            parsing_backslash=0
        else:
            if current_character == "\\":
                parsing_backslash=1
                abstract_syntax_tree_current_string = abstract_syntax_tree_current_string + current_character
            elif current_character == "(":
                debug("descending down in the abstract syntax tree")
                debug(abstract_syntax_tree_stack)
                #descend down in the abstract syntax tree
                new_array=[]
                if len(abstract_syntax_tree_current_string):
                    abstract_syntax_tree_stack[-1].append(abstract_syntax_tree_current_string )
                    abstract_syntax_tree_current_string=""

                abstract_syntax_tree_stack[-1].append(5)
                abstract_syntax_tree_stack[-1][-1]=new_array
                abstract_syntax_tree_stack.append(5)
                abstract_syntax_tree_stack[-1]=new_array

                debug(abstract_syntax_tree_stack)
            elif current_character == ")":
                #ascend up in the abstract syntax tree
                debug("asecending up the tree")
                debug(abstract_syntax_tree_stack)
                if len(abstract_syntax_tree_current_string):
                    abstract_syntax_tree_stack[-1].append(abstract_syntax_tree_current_string)
                    abstract_syntax_tree_current_string=""

                abstract_syntax_tree_stack=abstract_syntax_tree_stack[:-1]

                
                debug(abstract_syntax_tree_stack)
            else:
                abstract_syntax_tree_current_string = abstract_syntax_tree_current_string + current_character


    
    abstract_syntax_tree.pop(0)


    def change_newlines_to_space_in_abstract_syntax_tree (array):

        new_array=[]

        for current_ast_object in array:

            if type(current_ast_object) == str :

                new_string=""

                for character in current_ast_object :

                    if character == "\n":
                        new_string+=" "
                    else:
                        new_string = new_string + character
                new_array.append(new_string)
            else:
                new_array.append(change_newlines_to_space_in_abstract_syntax_tree(current_ast_object))
        return new_array



    abstract_syntax_tree=change_newlines_to_space_in_abstract_syntax_tree(abstract_syntax_tree)

    def remove_comments (array):

        new_array=[]

        for current_object in array:

            if type(current_object) == str:

                if current_object[0:8] == "comment ":
                    return []
                else:
                    new_array.append(current_object)
            else:
                new_array.append(remove_comments(current_object))

        return new_array


    abstract_syntax_tree=remove_comments(abstract_syntax_tree)

    def filter_whitespace_and_empty_array (array):

        new_array=[]
        for array_object in array:
            if type(array_object) == list:
                if len(array_object):
                    new_array.append(filter_whitespace_and_empty_array(array_object))
            else:
                is_whitespace_only=1
                for character in array_object:
                    if character != " ":
                        is_whitespace_only=0
                if not is_whitespace_only:
                    new_array.append(array_object)
        return new_array

    abstract_syntax_tree=filter_whitespace_and_empty_array(abstract_syntax_tree)
                
    def parse_symbols (array, number):
#        print(number)
        new_array=[]
        for array_object in array:
            if type(array_object) == list:
                new_array.append(parse_symbols(array_object, number + 1))
            else:
                string=""
                for character in array_object:
                    if character == " ":
                        if len(string):
                            new_array.append(string)
                        string=""
                    else:
                        string+=character
        return new_array


    abstract_syntax_tree=parse_symbols(abstract_syntax_tree, 0)
        
               
                    
                        
        
    

    print(abstract_syntax_tree)

if __name__ == "__main__":
    main()
