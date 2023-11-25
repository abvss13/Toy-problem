def exactly_two_positive(a, b, c):
    
    positive_count = sum(1 for num in (a, b, c) if num > 0)
    
    return positive_count == 2


result = exactly_two_positive(2, 4, -3)
print(result)  
