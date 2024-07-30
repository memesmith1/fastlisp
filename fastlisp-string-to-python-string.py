kestrel= lambda x : lambda y : x
kite= lambda x : lambda y : y
is_nil = (lambda l : (l(lambda h : (lambda t : ( lambda d : kite))) (kestrel)))

def bool_array_to_string(bool_array):
      # Ensure the length of bool_array is a multiple of 8
      if len(bool_array) % 8 != 0:
            raise ValueError("The length of the boolean array should be a multiple of 8.")
      
      # Split the boolean array into chunks of 8
      chunks = [bool_array[i:i+8] for i in range(0, len(bool_array), 8)]
      
      # Convert each chunk to a character and join them to form the final string
      result = ''.join([chr(int(''.join(['1' if bit else '0' for bit in chunk]), 2)) for chunk in chunks])
    
      return result

def fastlisp_string_to_python_sring(fastlisp_string):
      bool_array=[]
      while is_nil(fastlisp_string)(False)(True):
            bool_array = bool_array + [fastlisp_string(kestrel)(True)(False)]
            fastlisp_string=fastlisp_string(kite)
      return bool_array_to_string(bool_array)



