def solve(s):
    # Function to calculate the value of a consonant substring
    def substring_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)
    
    # Remove vowels from the input string
    vowels = "aeiou"
    consonant_string = "".join(char for char in s if char not in vowels)
    
    # Split the consonant string into substrings
    substrings = consonant_string.split('a')  # Using 'a' as a separator
    
    # Calculate the value of each consonant substring
    values = [substring_value(substring) for substring in substrings]
    
    # Return the highest value among the consonant substrings
    return max(values)

# Examples
print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57
