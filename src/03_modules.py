"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
if len(sys.argv) >= 1:
    for arg in sys.argv:
        print(arg)
else:
    print('no arguments given')

# Print out the OS platform you're using:
# YOUR CODE HERE
print('The os platform is ' + sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print('Python version ' + sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('the current process ID' + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print('current working directory ' + os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print('machine login name ' + os.getlogin()) 