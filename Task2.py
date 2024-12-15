def calculate_sum(file_path):
    try:
        total = 0
        with open(file_path, 'r') as file:
            for line in file:
                print(f"Reading line: {line.strip()}")
                total += int(line.strip())
        return total
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except ValueError:
        print(f"Error: File contains non-integer values.")
        return 0


file_path = 'numbers.txt'
print("Sum of integers:", calculate_sum(file_path))
