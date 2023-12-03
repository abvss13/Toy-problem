def two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

# Example usage:
result1 = two_positive(2, 4, -3)
result2 = two_positive(-4, 6, 8)
result3 = two_positive(4, -6, 9)

print(result1)  # Output: True
print(result2)  # Output: True
print(result3)  # Output: True
