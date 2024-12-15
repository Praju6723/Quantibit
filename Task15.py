def optimized_code(numbers):
    result = []
    
    squares = [f"Square of {num} is {num ** 2}" for num in numbers if num % 2 == 0]
    result.extend(squares)
    
    max_num = max(numbers, default=None)
    result.append(f"\nMax number is {max_num}")
    
    count_dict = {num: numbers.count(num) for num in set(numbers)}
    result.append("Number counts:")
    for num, count in count_dict.items():
        result.append(f"{num}: {count}")
    
    return "\n".join(result)
