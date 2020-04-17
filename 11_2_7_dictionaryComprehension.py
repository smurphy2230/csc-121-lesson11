#  with dictionary comprehensions it is possible to create dictionaries at runtime using concise  #  syntax.
#  create a dictionary which uses integers as keys and their cubes as values
cubes = {x: x**3 for x in range(5)}
print(cubes)
print()
#  create dictionary of even squares
squares = {y: y**2 for y in range(13) if y % 2 == 0}
print(squares)