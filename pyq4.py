import matplotlib.pyplot as plt
from collections import Counter

try:
    # Read file content
    with open('file.txt', 'r') as f:
        text = f.read()

    # Count characters (excluding whitespace)
    char_counts = Counter(char for char in text if not char.isspace())
    
    # Sort characters and their counts
    chars = list(char_counts.keys())
    counts = list(char_counts.values())

    # Create histogram
    plt.figure(figsize=(12, 6))
    plt.bar(chars, counts, color='skyblue')

    # Customize plot
    plt.title('Character Frequency in File')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')

    # Add value labels on top of bars
    for i, count in enumerate(counts):
        plt.text(i, count, str(count), ha='center', va='bottom')

    # Show plot
    plt.show()

except FileNotFoundError:
    print("Error: file.txt not found!")
except Exception as e:
    print(f"An error occurred: {e}")
