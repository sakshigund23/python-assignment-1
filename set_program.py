#2.1 Create and access set elements 
set1={10,20,30,40}
set2={30,40,50,60}

print("Set 1:", set1)
print("Set 2:", set2)

#Accessing elements (using loop because sets are unordered)
print("Element of set 1:")
for element in set1:
    print(element)

#2.2 Union of set 1 and set 2
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# 2.3 Intersection of the elements
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# 2.4 Difference of the elements
difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2:", difference_set)