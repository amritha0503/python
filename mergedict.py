# Input lists from user
keys = input("Enter the keys (comma-separated): ").split(',')
values = input("Enter the values (comma-separated): ").split(',')

# Initialize empty dictionary
merged_dict = {}

# Merge lists into dictionary
for i in range(len(keys)):
    merged_dict[keys[i].strip()] = values[i].strip()

# Print the resulting dictionary
print("Merged Dictionary:", merged_dict)
