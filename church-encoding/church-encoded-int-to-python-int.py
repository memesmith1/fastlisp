kestrel = lambda x : lambda y : x
kite = lambda x : lambda y : y
pred=lambda n : lambda f : lambda x : n(lambda g : lambda h : (h((g)(f))))(lambda u : x) (lambda u : u)
iszero=lambda n : (n)(lambda x : kite)(kestrel)
def church_encoded_int_to_python_int(church_encoded_int):
    counter=0
    while iszero(church_encoded_int)(False)(True) :
        counter=counter+1
        church_encoded_int=pred(church_encoded_int)

    return counter
