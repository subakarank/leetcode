'''
Given a  string, write a method that returns true if the string is a valid number or false otherwise.
 Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, "-" and ".". The string can be very long (think millions of characters) and no built-in function/class can handle it without overflowing or losing precision.

Some example strings and expected output:

"13"    ---> true
"3.0"   ---> true
"-7.4"  ---> true
"-13.5" ---> true
"abc"   ---> false
"123a"  ---> false
"-."    ---> false  # here
"-..--" ---> false
"1.0.0.1" -> false

#Facebook question

'''

def is_digit(char):
    return '0' <= char <= '9'

def is_string_valid_number(s: str) -> bool:
    negative_counter = 0
    decimal_counter = 0
    if s == '.' or s == '-' or s == '.-' or s == '-.':
        return False
    for i, char in enumerate(s):
        if is_digit(char):
            continue
        elif char == '-':
            if i != 0 :
                return False
            negative_counter += 1
            if negative_counter > 1 :
                return False
        elif char == '.':
            decimal_counter += 1
            if decimal_counter > 1:
                return False
        else:
            return False
    return True

print(f"is_string_valid_number('13'): {is_string_valid_number("13")}")      # True
print(f"is_string_valid_number('3.0'): {is_string_valid_number("3.0")}")     # True
print(f"is_string_valid_number('-7.4'): {is_string_valid_number("-7.4")}")    # True
print(f"is_string_valid_number('-13.5'): {is_string_valid_number("-13.5")}")   # True
print(f"is_string_valid_number('abc'): {is_string_valid_number("abc")}")     # False
print(f"is_string_valid_number('123a'): {is_string_valid_number("123a")}")    # False
print(f"is_string_valid_number('-. '): {is_string_valid_number("-. ")}")     # False
print(f"is_string_valid_number('-..--'): {is_string_valid_number("-..--")}")   # False
print(f"is_string_valid_number('1.0.0.1'): {is_string_valid_number("1.0.0.1")}") # False
