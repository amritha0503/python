def remove_matching_letter(l1, l2):
    for letter in set(l1):  # Use set to avoid duplicates and improve efficiency
        if letter in l2:
            l1.remove(letter)
            l2.remove(letter)
            return [l1 + ['*'] + l2, True]
    return [l1 + ['*'] + l2, False]

# Get input from users
p1 = input("Enter the first person's name: ").lower().replace(" ", "")
p2 = input("Enter the second person's name: ").lower().replace(" ", "")

l1 = list(p1)
l2 = list(p2)
proceed = True

# Main loop to remove matching letters
while proceed:
    ret_list = remove_matching_letter(l1, l2)
    con_list = ret_list[0]
    proceed = con_list[1]
    star_index = con_list.index('*')
    l1 = con_list[:star_index]
    l2 = con_list[star_index + 1:]

# Count remaining letters
count = len(l1) + len(l2)
result = ['friends', 'love', 'affection', 'marriage', 'enemy', 'siblings']

# Calculate the relationship type based on the count
if count == 0:
    relationship = "No relationship found!"
else:
    split_index = (count % len(result)) - 1
    if split_index >= 0:
        relationship = result[split_index + 1:] + result[:split_index + 1]
    else:
        relationship = result[-1:]  # Handle case where count is 0

print("The relationship is:", relationship[0])
