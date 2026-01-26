#1.1 Create and access list elements 
my_list = [10,20,30,40,50]
print("Original List:" , my_list)

print("First element:" , my_list[0])
print("Third element:" , my_list[2])

#1.2 Add and remove list elements 
#Adding elements 
my_list.append(60)
print("After adding 60:" , my_list)
my_list.insert(2,25)
print("After inserting 25 at index 2 :" , my_list)

#Remove elements
my_list.remove(40)
print("After removing 40:" , my_list)
print("After popping last elements:" , my_list)

#1.3 Sort list elements
my_list.sort()
print("Sorted list:" , my_list)

#1.4 Reverse list element
my_list.reverse()
print("Reversed List:" , my_list)