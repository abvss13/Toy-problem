def solve(word):
    vowels = "aeiou"
    max_consonant_value = 0
    current_consonant_value = 0

    for char in word:
        if char not in vowels:
            current_consonant_value += ord(char) - ord('a') + 1
        else:
            max_consonant_value = max(max_consonant_value, current_consonant_value)
            current_consonant_value = 0

    return max(max_consonant_value, current_consonant_value)

# Example usage:
result1 = solve("zodiacs")
result2 = solve("strength")

print(result1)  # Output: 26
print(result2)  # Output: 57
