ibis = lambda x : x

kestrel = lambda x : lambda y x

kite = lambda x : lambda y : y

viero = lambda x : lambda y : lambda z : z(x)(y)

z = lambda f : (lambda x : f(lambda v : x(x)(v)))(lambda x : f(lambda v : x(x)(v)))
