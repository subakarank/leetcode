def square_root_brute_force(x):
    if x == 0:
        return 0

    for i in range(1, x + 1):
        if i * i > x:
            return i - 1
    
    return x

# Example usage
print(square_root_brute_force(8))  # Output: 2
print(square_root_brute_force(10)) # Output: 3



def square_root(x:int):
    if x == 0: 
        return 0 
    left, right = 1 , x
    while left <= right:
        mid = ( left + right ) // 2 
        if mid * mid == x:
            return mid
        elif mid * mid < x : 
            left = mid + 1
        else:
            right = mid -1
    return right 

print(square_root(10))  # Output: 3

'''
    Newton's Method (Optimal)
'''

def my_sqrt_newton(x):
    if x == 0:
        return 0
    guess = x
    while True:
        new_guess = (guess + x / guess) // 2
        if new_guess == guess:
            return int(guess)
        guess = new_guess

# Example usage
print(my_sqrt_newton(8))  # Output: 2
print(my_sqrt_newton(10)) # Output: 3




