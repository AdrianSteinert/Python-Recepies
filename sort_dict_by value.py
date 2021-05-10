import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print("Using lambda: {0}".format(sorted(xs.items(), key=lambda x: x[1])))

print()

# by using operator

print("Using operator function: {0}".format(sorted(xs.items(), key=operator.itemgetter(1))))
