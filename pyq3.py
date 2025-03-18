import matplotlib.pyplot as plt

# Simple data
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 8, 5, 7, 6]

# Create bar plot
plt.figure(figsize=(10, 5))
plt.bar(categories, values, color='skyblue')

# Add value labels on top of bars
for i, v in enumerate(values):
    plt.text(i, v, str(v), ha='center', va='bottom')

# Add labels and title
plt.title('Simple Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show plot
plt.show()