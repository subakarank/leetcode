import math
def pow_math(x, n ):
    return math.pow(x, n )

# result = pow_math(2, 5)
# print(result)  # Output: 32.0

# result = pow_math(3, -3)
# print(result) # Output: 0.037037037037037035

def pow_brute_force(x,n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    for _ in range(n):
        result *= x
    return result
# result = pow_brute_force(2, 5)
# print(f"pow_brute_force {result}")  # Output: 32.0

# result = pow_brute_force(3, -3)
# print(f"pow_brute_force {result}") # Output: 0.037037037037037035


def pow_recursive(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x 
        return pow_recursive(x, -n)
    elif n % 2 == 0:
        half_pow = pow_recursive(x, n//2)
        return half_pow * half_pow
    else: 
       return x * pow_recursive(x, n-1)
    
result = pow_recursive(2, 5)
print(f"pow_recursive {result}")  # Output: 32.0

result = pow_recursive(3, -3)
print(f"pow_recursive {result}") # Output: 0.037037037037037035
    
def pow_interate(x, n ):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x 
        n = -n
    result = 1
    while n > 0 :
        if n % 2 == 1:
            result *= x 
        x *= x
        n = n // 2 