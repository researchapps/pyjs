def i(x):
    return x

class Foo:
    pass

def test_builtins():
    x = []
    y = callable(x)
    z = list(map(i, x))
    list(filter(callable, z))
    dir(x)
    if hasattr(x, "foo"):
        foo = getattr(x, "foo")

    f = Foo()
    setattr(f, "bar", 42)
    if hasattr(f, "bar"):
        bar = getattr(f, "bar")

test_builtins()
