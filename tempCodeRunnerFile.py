def remove_matching_letter(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                return [l1 + ['*'] + l2, True]
    return [l1 + ['*'] + l2, False]

p1 = input("Enter the first person's name: ").lower().replace(" ", "")
p2 = input("Enter the second person's name: ").lower().replace(" ", "")

l1 = list(p1)
l2 = list(p2)
proceed = True

while proceed:
    ret_list = remove_matching_letter(l1, l2)
    con_list = ret_list[0]
    proceed = con_list[1]
    star_index = con_list.index('*')
    l1 = con_list[:star_index]
    l2 = con_list[star_index + 1:]

count = len(l1) + len(l2)
result = ['friends', 'love', 'affection', 'marriage', 'enemy', 'siblings']

# Calculate the split index
split_index = (count % len(result)) - 1
if split_index >= 0:
    right = result[split_index + 1:]
    left = result[:split_index + 1]
    result = right + left
else:
    result = result[:len(result) - 1]

print("The relationship is:", result[0])
