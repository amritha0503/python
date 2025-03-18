import matplotlib.pyplot as plt

# Lists to store data
programminglang = []
popularity = []

# Read data from file
try:
    with open('file.txt', 'r') as file:
        for line in file:
            # Split each line into language and value
            lang, value = line.strip().split(',')
            programminglang.append(lang)
            popularity.append(float(value))

    # Create color list
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

    # Create bar chart
    plt.figure(figsize=(10, 5))
    bars = plt.bar(programminglang, popularity, color=colors)

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}%', ha='center', va='bottom')

    # Customize the chart
    plt.title('Programming Language Usage')
    plt.xlabel('Programming Language')
    plt.ylabel('Popularity (%)')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.show()

except FileNotFoundError:
    print("Error: language_data.txt not found!")
except Exception as e:
    print(f"An error occurred: {e}")