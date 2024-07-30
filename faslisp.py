//if, quote

ibis = lambda x : x
lambda_if = ibis
quote = ibis

//true, or, head
kestrel = lambda x : lambda y x
lambda_true = kestrel
lambda_or = lambda x : lambda y : x(kestrel)(y)
head = lambda list : list(kestrel)

//false, and, tail
kite = kestrel(ibis)
lambda_false = kite
lambda_and = lambda x : lambda y : x(y)(kestrel)
tail = lambda list : list(kite)

//not
lambda_not = lambda x : x(kite)(kestrel)

//pair, cons, tuple
viero = lambda x : lambda y : lambda z : z(x)(y)
is_nil = (lambda l : (l(lambda h : (lambda t : ( lambda d : kite))) (kestrel)))

//recurse with an argument
z = lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v)))
