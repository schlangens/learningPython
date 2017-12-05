# Iterable means can be looped through

# Split method by default breaks on white space

print('hello there students'.split())

# outputs 3 items into a list ['hello' , 'there' , 'students']

# we can tell it what to break on
print("red:blue:green".split(':'))


flavors = ['chocolate', 'mint', 'strawberry']

print("My favorite flavors are: {}".format(", ".join(flavors)))

# You can only join string items