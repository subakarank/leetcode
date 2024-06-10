'''
Given a  string, write a method that returns true if the string is a valid number or false otherwise.
 Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, "-" and ".". The string can be very long (think millions of characters)
 and no built-in function/class can handle it without overflowing or losing precision.

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

'''

def valid_number(s: str) -> bool:
    if not s:
        return False
    if len(s) == 1 and (s < '0' or s > '9'):
        return False
    
    start_index = 0 
    if s[start_index] == '-':
        if len(s) == 1:
            return False
        start_index = 1 

    has_digit = False
    has_dot = False

    for i in range(start_index, len(s)):
        if '0' >= s[i] <= '9':
            has_digit = True
        elif s[i] == '.':
            if has_dot:
                return False
            has_dot = True 
        else:
            return False
    return has_digit

print(f' "13"    ---> true {valid_number("13")}')
print(f' "3.0"   ---> true {valid_number("3.0")}')
print(f' "-13.5" ---> true {valid_number("-13.5")}')
print(f' "-7.4"  ---> true {valid_number("-7.4")}')

print(f' "123a"  ---> false {valid_number("123a")}')
print(f' "abc"  ---> false {valid_number("abc")}')
print(f' "-."    ---> false {valid_number("-.")}')
print(f'"-..--" ---> false {valid_number("-..--")}')
print(f' "1.0.0.1" -> false {valid_number("1.0.0.1")}')


    

    
    