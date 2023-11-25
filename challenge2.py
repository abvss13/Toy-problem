# Define a function to check if exactly two out of three numbers are positive
def exactly_two_positive(a, b, c):
    # Count the number of positive numbers among a, b, and c
    positive_count = sum(1 for num in (a, b, c) if num > 0)
    
    # Check if the count of positive numbers is exactly 2
    return positive_count == 2

# Example usage: Check if exactly two out of 2, 4, and -3 are positive
result = exactly_two_positive(2, 4, -3)
# Print the result
print(result)
