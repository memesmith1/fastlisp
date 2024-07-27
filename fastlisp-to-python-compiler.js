/*

Copyright (C) 2024 by John Morris Beck <john.morris.beck@hotmail.com>

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL

IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER

RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF

THIS SOFTWARE.

*/

var input=`(comment fastlisp sample code)

(comment primitives)
(comment names)
(lambda ibis
(lambda kestrel
(lambda kite
(lambda viero
(lambda z

(comment renaming primitives)
(lambda undefined
(lambda if
(lambda quote
(lambda true
(lambda false
(lambda pair
(lambda first
(lambda second
(lambda recurse
(lambda not
(lambda or
(lambda and

(comment undefined function names)
(lambda eval
(lambda +
(lambda -
(lambda *
(lambda /
(lambda ^
(lambda <
(lambda >
(lambda <=
(lambda >=

(comment undefined python functions)
(lambda get_subobject

(comment sample program names)
(lambda is-old-enough?

(comment main program)
undefined

(comment definitions)

(comment is-old-enough?)
) (lambda age
          (if (>= age
                  (text 18)
               )
               true
               false
))

(comment get_subobject)
) (comment text)
  (lambda object_name
          (lambda string
                  (concatenate (text getattr\()
                               object_name
                               (text  , ")
                               string
                               (text "\))

(comment >=)
) undefined

(comment <=)
) undefined

(comment >)
) undefined

(comment <) 
) undefined

(comment ^)
) undefined

(comment /)
) undefined

(comment *)
) undefined

(comment -)
) undefined

(comment +)
) undefined

(comment so basically eval with the current design of fastlisp is unable to be contextually aware of the variable names that we are defining because these veriable names only exist before compile time
         so if we are going to eval we have to do it with a new fastlisp program unless we use macros.
)
(comment eval)
) (lambda new-fastlisp-program-in-a-string
          undefined)

(comment and)
) (lambda x (lambda y (x y and)))

(comment or)
) (lambda x (lambda y (x kestrel y)))

(comment not)
) (lambda x (x true false))

(comment recurse)
) z

(comment second)
) kite

(comment first)
) kestrel


(comment pair)
) viero

(comment false)
) kite

(comment true)
) kestrel

(comment quote)
) ibis

(comment if)
) ibis

(comment undefined)
) kite

(comment z)
) (lambda f
        ((lambda x 
                 (f (lambda v
                            (x x v))))
         (lambda x 
                 (f (lambda v
                            (x x v))))))

(comment viero)
) (lambda x
          (lambda y
                  (lambda z
                          (z x y))))

(comment kite)
) (kestrel ibis)

(comment kestrel)
) (lambda x
          (lambda y
                  x))

(comment ibis)
) (lambda x
          x)

`;


/*

the first thing we wanna do is remove the comments

*/

var new_input="";

var parentheses_depth_counter=0;

for(var i = 0; i < input.length; i++){

    switch(input.charAt(i)){

    case '(':

	/*
	  check to see if the current parentheses in the tree is a comment

	 */
	var is_comment=1;
	var comment_text="(comment ";
	for(var j=0; j <  9 ; j++){
	    if(comment_text.charAt(j) != input.charAt(i+j)){
		is_comment=0;
	    }
	}

	//now if it is a comment the is_comment should be 1 and if it is not a comment the is_comment should be 0

	if(is_comment){
	    /*

	      if it is a comment then we are gonna walk down the tree that is inside of the comment and skip it

	    */
	    var comment_parentheses_depth_end = parentheses_depth_counter - 1  ;
	    
	    i++;


	    for(;parentheses_depth_counter > comment_parentheses_depth_end; i++){
	
		switch(input.charAt(i)){

		case '(':

		    parentheses_depth_counter++;

		    break;

		case ')':

		    parentheses_depth_counter--;

		    break;

		default:

		    break;


		}
		
	    }

	}
	else{

	    /*
	      
	      if it is not a comment then we are going to add it to the new_input
	      
	    */

	    parentheses_depth_counter++;
	    new_input=new_input.concat(input.charAt(i));
	    

	}
	

	break;

    case ')':
	parentheses_depth_counter--;
	new_input=new_input.concat(input.charAt(i));
	break;
	
    default:

		new_input=new_input.concat(input.charAt(i));

	break;
	
    }
    

}

console.log(new_input);


/*

the second thing we wanna do is we wanna convert the strings into lists of booleans

*/
/*

var convert_character_to_binary_string=character=>character.charCodeAt(0).toString(2);


input=new_input;
new_input="";

var parentheses_depth_counter=0;

for(var i = 0; i < input.length; i++){

    switch(input.charAt(i)){

    case '(':
	parentheses_depth_counter++;

*/
	/*
	  check to see if the current parentheses in the tree is a comment

	*/
/*
	var is_text=1;
	var text_text="(text ";
	for(var j=0; j <  5 ; j++){
	    if(text_text.charAt(j) != input.charAt(i+j)){
		is_text=0;
	    }
	}


	if(is_text){
	    console.log("it was text\n");

*/
	    /*

	      if it is a string we're going to convert it to a list of booleans

	    */
/*
	    i+=5;


	    var continue_parsing_string=1;
	    for(;continue_parsing_string;i++){

*/

		/*

		  this variable has to be recorded because for each bit in the string we need another
		  closing parentheses. ideally a better string encoding can be found.

		*/

/*
		var string_bit_length=0;

		switch(input.charAt(i)){

		case ')':

		    for(var j=0; j<string_bit_length; j++){

			input=input.concat(")");
		    }

		    continue_parsing_string=0;

		    break;

		case '\\':

		    switch(input.charAt(++i)){
		    case ')':
		    case '\\':
  		 	var binary_string=convert_character_to_binary_string(input.charAt(i));
			for(var i=0; i < binary_string.length; i++){

			    string_bit_length++;
			    
			    switch(binary_string.charAt(i)){

			    case '0':

				input=input.concat("(viero kite ");

				break;


			    case '1':

				input = input.concat( "(viero kestrel " );

				break;

			    default:
				
				((x=>x/0)(5));

				break;

			    }

			}
			
			break;

			    default:
			    (x=>x / 0)(420);

			    break;

			}

		    break;

		default:

			var binary_string=convert_character_to_binary_string(input.charAt(i));
			for(var i=0; i < binary_string.length; i++){

			    string_bit_length++;
			    
			    switch(binary_string.charAt(i)){

			    case '0':

				input=input.concat("(viero kite ");

				break;


			    case '1':

				input = input.concat( "(viero kestrel " );

				break;

			    default:
				
				(x=>x/0)(5);

				break;

			    }

			}
			
			break;

			}


		    break;



		    }


	}
	else{

*/

	    /*
	      
	      if it is not text then we are going to add it to the new_input
	      
	    */

/*

	    parentheses_depth_counter++;
	    new_input=new_input.concat(input.charAt(i));
	    

	}
    

    }


}

*/

var convert_character_to_binary_string = character => character.charCodeAt(0).toString(2).padStart(8, '0');

input = new_input;
new_input = "";


for (var i = 0; i < input.length; i++) {
    if (input.startsWith("(text ", i)) {
	var number_of_closing_parens=0;
        i += 5;  // Skip "(text "
        while (input[i] !== ')') {
            var binary_string = convert_character_to_binary_string(input[i]);
            for (var bit of binary_string) {
		number_of_closing_parens++
                new_input += (bit === '0') ? "(viero kite " : "(viero kestrel ";
            }
            i++;
        }
	for(var j=0; j < number_of_closing_parens; j++){
            new_input += ")";
	}
    } else {
        new_input += input[i];
    }
}

console.log(new_input);

//    console.log(input);


var lambda_true = x=>y=>x;
var lambda_false = x=>y=>y;
var lambda_pair = x=>y=>z=>z(x)(y);


/*

the third thing we wanna do is convert the single lambda expression that remains into a python lamdba expression

*/
