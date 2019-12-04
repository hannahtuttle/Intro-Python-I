"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('Using printf x: %d, y: %s, z: %s' % (10, round(y, 2), z))

# Use the 'format' string method to print the same thing
print('Using format x: {}, y:{}, z:{}'.format(x, round(y, 2), z))

# Finally, print the same thing using an f-string

print(f'Using f-string X: {x} Y: {round(y, 2)} Z: {z}')