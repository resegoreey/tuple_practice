#Tuple Creation
print("We will be using this tuple throughout the programs")
clothing = ("Shirt", "Skirt", "Pants", "Jeans", "Shorts", "Socks", "Sweater", "Hoodie")
print(clothing)
print()

#Accessing Tuple Elements
#accessing the first item of the tuple
print(f"The first item is: {clothing[0]}")
#accessing the last item of the tuple
print(f"The last item is: {clothing[-1]}")
print()

#Tuple Slicing
#user determines the range to slice the tuple
range1 = int(input("Enter the 1st range(0-8): "))
range2 = int(input("Enter the 2nd range(0-8): "))
#getting the subsets items
subset = clothing[range1:range2]
print(f"Clothing = {subset}")
print()

#Tuple Concatenation
# We will concatinate the original tuple and the subset we created
apparels = clothing + subset
print(f"Concatinated tuples = {apparels}")
print()

#Tuple Unpacking
#we will unpack the clothing tuple into 4 variables
(w, x, *y , z) = clothing
print(f"Unpacked w = {w}")
print(f"Unpacked x = {x}")
print(f"Unpacked y = {y}")
print(f"Unpacked z = {z}")
print()

# Convert Tuple to List
#we will use the clothing tuple still
clothing_list = list((clothing))
#adding an item
clothing_list[2] = "Bikini"
#removing an item
clothing_list.remove("Socks")
clothing = tuple((clothing_list))
print(clothing)