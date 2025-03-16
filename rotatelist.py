# Input the list from the user
user_list = input("Enter the elements of the list separated by space: ").split()

# Input the value of k (number of positions to rotate)
k = int(input("Enter the number of positions to rotate: "))

# Normalize k to ensure it is within the length of the list
k = k % len(user_list)

# Rotate the list by slicing and concatenating
rotated_list = user_list[-k:] + user_list[:-k]

# Print the result
print("The rotated list is:", rotated_list)
