def reverse_integer(x: int) -> int:

    result = 0
    min_int, max_int = -2 ** 31, 2 ** 31 - 1
    is_negative = x < 0 
    x = abs(x)

    # 123 
    while x != 0: 
        digit = x % 10
        if result > (max_int - digit ) // 10:
            return 0 
        result = result * 10 + digit # 3 # 32 # 321 
        x = x // 10
    
    if result < min_int or result > max_int:
        return 0 
    if is_negative:
        result = -result 

    return result 

    
x = -123
print("input", x)
print("output:", reverse_integer(x))

'''
x = 123 
3

1 X 10(2) + 2 X 10(1) + 3 X 10(0)
1 X 100 + 2 X 10 + 3 X 1
100 + 20 + 3

3 X 10 X 10  = 300 

result * 10 + digit <= max_int
result * 10 <= max_int - digit 
result <= (max_int - digit ) // 10
'''
