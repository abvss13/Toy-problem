# Function to check if exactly two out of three numbers are positive
def two_are_positive(a, b, c):
    # Initialize a counter to keep track of the number of positive numbers
    positive_count = 0
    
    # Check if the first number (a) is positive
    if a > 0:
        positive_count += 1
        
    # Check if the second number (b) is positive
    if b > 0:
        positive_count += 1
        
    # Check if the third number (c) is positive
    if c > 0:
        positive_count += 1
        
    # Return True if exactly two numbers are positive, otherwise return False
    return positive_count == 2

# Example usage of the function with different sets of numbers
print(two_are_positive(-1, 2, -4))  # Output: True (exactly two numbers are positive)
print(two_are_positive(-1, 2, 3))   # Output: False (more than two numbers are positive)
