
def array(f):
    def dec(*args, **kwargs):
        print(args, kwargs)
        a = f(*args, **kwargs)
        return a.split(' ')
    return dec


@array
def name():
    return "Shubham Sinha is an asshole"


a = name()
print(a)


y = "shubham sinha"
a = y.split(" ")

print(a)


class Trace:
    def __init__(self):
        self.name = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.name:
                print("tracing")
            else:
                print("T")
            return f(*args, **kwargs)
        return wrap


tracer = Trace()


@tracer
def rotate(l):
    return l[1:] + [l[0]]

l = [1,2,3]

a = rotate(l)

tracer.name = True

a = rotate(l)

tracer.name = False

a = rotate(l)



