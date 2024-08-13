def reverse_except_3rd_and_6th(group):
    # Convert the input string into a list of individual characters (digits)
    numbers = list(group)
    
    if len(numbers) != 8:
        raise ValueError(f"Each group must contain exactly 8 digits, but got {len(numbers)} characters.")
    
    # Extract the 3rd and 6th digits
    third_digit = numbers[2]
    sixth_digit = numbers[5]
    
    # Reverse the other digits
    reversed_group = [
        numbers[7],  # 8th digit
        numbers[6],  # 7th digit
        third_digit,  # 3rd digit (unchanged)
        numbers[4],  # 5th digit
        numbers[3],  # 4th digit
        sixth_digit,  # 6th digit (unchanged)
        numbers[1],  # 2nd digit
        numbers[0]   # 1st digit
    ]
    
    return reversed_group

def process_groups(input_str):
    groups = input_str.split()  # Split by spaces to get each group
    
    processed_groups = []
    for group in groups:
        processed_groups.append(reverse_except_3rd_and_6th(group))
    
    return processed_groups

# Example usage:
input_str = "12345678 87654321"
try:
    result = process_groups(input_str)
    for group in result:
        print("".join(group))  # Join the list back into a string of digits
except ValueError as e:
    print(e)
