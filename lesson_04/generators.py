def foo():
    print('im foo')

def bar():
    print('im bar')


def baz():
    yield 1
    yield 2
    yield 3
    yield 4



gen = baz()

print (next(gen))
gen.send(98)
print (next(gen))
print (next(gen))
print (next(gen))
print ('end')