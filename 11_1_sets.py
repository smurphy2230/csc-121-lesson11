#  a set is a group of unordered values with no duplicates. provides the usual mathmetical set
#  operations; union, intersection, difference and symmetric difference.
#  created by enclosing elements with {}
#  -------------------------------
#  fruit = {'apple', 'banana', 'pear', 'peach'}
#  print('Elements in the fruit set: ', fruit)
#  # create an empty set by calling the set function
#  vegetables = set()  # create empty set
#  vegetables.add('brocolli')
#  vegetables.add('spinach')
#  vegetables.add('carrot')
#  vegetables.add('cabbage')
#  vegetables.add('kale')
#  vegetables.add('potato')
#  vegetables.add('peas')
#  print('Elements in the vegetable set: ', vegetables)
#  fruit.remove('pear')
#  vegetables.remove('cabbage')
#  print('Elements in the fruit set after remove: ', fruit)
#  print('Elements in the vegetable set after remove: ', vegetables)
#  print()
#  fruit.add('pear')
#  vegetables.add('cabbage')
#  print('Elements in the fruit set: ', fruit)
#  print('Elements in the vegetable set: ', vegetables)
#  print()
#  length_fruit = len(fruit)
#  print('Number on elements in fruit set: ', length_fruit)
#  length_vegetables = len(vegetables)
#  print('Number of elements in vegatables set: ', length_vegetables)
#  print()
# -----------------------------------
#  mathematical set operations: union, intersection, difference, symmetric difference
#  set_A = {'apple', 'banana', 'pear', 'peach'}
#  set_B = {'orange', 'banana', 'grape', 'pear'}
#
#  print("set_A", set_A)
#  print("set_B", set_B)
#  print()
#  print("A union B", set_A | set_B)
#  print("A intersect B", set_A & set_B)
#  print("A - B", set_A - set_B)
#  print("B - A", set_B - set_A)
#  print("Symmetric difference: ", set_A ^ set_B)
#  print()
#  -----------------------------------
#  create set from list or tuple
#  fruit_list = ['apple', 'banana', 'pear', 'peach']
#  fruit = set(fruit_list)
#  print("Elements in the set: ", fruit)
#  create a tuple or list from a set
fruit_set = {'apple', 'banana', 'peach', 'pear'}
fruit_list = list(fruit_set)
print("Elements in the list: ", fruit_list)
fruit_tuple = tuple(fruit_set)
print("Elements in the tuple: ", fruit_tuple)
print()
#  set comprehensions are identical to list comprehensions, they use curly braces instead of square #  brackets
squ_set = {x**2 for x in range(13) if x % 2 == 0}
print(squ_set)
