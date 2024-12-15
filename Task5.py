def validate_integer_input(user_input):
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a number.")


validate_integer_input("abc")  
validate_integer_input("123")  