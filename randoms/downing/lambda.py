# making a closure
def make_inc_b(j):
    return lambda i: i+j

a = make_inc_b(1)
print(a(2))
