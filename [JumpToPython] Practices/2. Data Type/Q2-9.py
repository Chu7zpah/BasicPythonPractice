# Dictionary Grammar Problem

a = dict()

# Which of these statements causes an error?
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'

# a[[1]] = 'python'
# Occurs an error since [1] (list) is a MUTABLE value
# Dictionary's key only use IMMUTABLE(String, Int, Tuples..) values
# TypeError: unhashable type: 'list' (Unhashable == mutable)
