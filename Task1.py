def reverse_string(string):
    reversed_str = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

input_string = "hello"
output_string = reverse_string(input_string)
print("Input:", input_string)
print("Output:", output_string)
