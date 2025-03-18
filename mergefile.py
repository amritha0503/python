# Initialize empty list for all numbers
all_numbers = []

# Read from first file
try:
    with open('file1.txt', 'r') as file1:
        for line in file1:
            numbers = line.strip().split()
            for num in numbers:
                all_numbers.append(int(num))
except FileNotFoundError:
    print("file1.txt not found!")

# Read from second file
try:
    with open('file2.txt', 'r') as file2:
        for line in file2:
            numbers = line.strip().split()
            for num in numbers:
                all_numbers.append(int(num))
except FileNotFoundError:
    print("file2.txt not found!")

# Read from third file
try:
    with open('file3.txt', 'r') as file3:
        for line in file3:
            numbers = line.strip().split()
            for num in numbers:
                all_numbers.append(int(num))
except FileNotFoundError:
    print("file3.txt not found!")

# Sort the numbers
all_numbers.sort()

# Write sorted numbers to new file
try:
    with open('merged_sorted.txt', 'w') as outfile:
        for number in all_numbers:
            outfile.write(str(number) + '\n')
    print(f"Successfully merged and sorted {len(all_numbers)} numbers")
    print("Results written to merged_sorted.txt")
except Exception as e:
    print(f"Error writing to output file: {e}")