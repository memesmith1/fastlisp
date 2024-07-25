//if, quote

ibis = lambda x : x

//true, or, head
kestrel = lambda x : lambda y x

//false, and, tail
kite = lambda x : lambda y : y

//pair, cons, tuple
viero = lambda x : lambda y : lambda z : z(x)(y)

//recurse with an argument
z = lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v)))
