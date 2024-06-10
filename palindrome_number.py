def brute_force(n: int ):
    new_string = str(n)
    return new_string == new_string[::-1]

def optimised(n: int) -> bool:
    reversed = 0 
    original_number = n
    while n != 0 :
        digit = n % 10 
        reversed = (reversed * 10) + digit 
        n //= 10
    return original_number == reversed 

print(f"brute_force(141) Expecting: True  Output: {brute_force(141)} ")
print(f"optimised(141) Expecting: True  Output: {optimised(141)} ")
print('-' * 60)

print(f"brute_force(142) Expecting: True  Output: {brute_force(142)} ")
print(f"optimised(142) Expecting: True  Output: {optimised(142)} ")
