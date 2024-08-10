# test-garbage
def reverse_except_3rd_and_6th(group):
    # Convert the input string of numbers into a list of integers
    numbers = list(map(int, group.split()))
    
    if len(numbers) != 8:
        raise ValueError("Each group must contain exactly 8 numbers")
    
    # Reverse the numbers while keeping the 3rd and 6th numbers in place
    reversed_group = [numbers[7], numbers[6], numbers[2], numbers[5], numbers[4], numbers[3], numbers[1], numbers[0]]
    
    return reversed_group

def process_groups(input_str):
    groups = input_str.split('  ')  # Assuming groups are separated by double spaces
    
    processed_groups = []
    for group in groups:
        processed_groups.append(reverse_except_3rd_and_6th(group))
    
    return processed_groups

# Example usage:
input_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"
result = process_groups(input_str)

for group in result:
    print(" ".join(map(str, group)))
