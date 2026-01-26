# 3.1 Create and access tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 3.2 Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)

print("Access element from nested tuple:", nested_tuple[2][1])

# 3.3 Repetition of tuple
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# 3.4 Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)