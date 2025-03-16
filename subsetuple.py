# Input the first tuple from the user
tuple1 = tuple(input("Enter the elements of the first tuple separated by space: ").split())

# Input the second tuple from the user
tuple2 = tuple(input("Enter the elements of the second tuple separated by space: ").split())

# Check if tuple2 is a subset of tuple1
is_subset = True
for element in tuple2:
    if element not in tuple1:
        is_subset = False
        break

# Print the result
if is_subset:
    print("The second tuple is a subset of the first tuple.")
else:
    print("The second tuple is not a subset of the first tuple.")
