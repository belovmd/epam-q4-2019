"""Tuple practice"""
# 1
lst = ['a', 'b', 'c']
tpl = tuple(lst)

# 2
tpl = ('a', 'b', 'c')
lst = list(tpl)

print("{}: {}".format(type(lst), lst))
print("{}: {}\n".format(type(tpl), tpl))

# 3
a, b, c = ('a', 2, 'gamma')
print("{}; {}; {}\n".format(a, b, c))

# 4
tpl = (('a', 'b', 'c'), )
print("tuple length: {}".format(len(tpl)))
