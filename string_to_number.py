def to_number(n: str) -> int:
    num = 0
    for char in n:
        digit = ord(char) - ord('0')
        num = num * 10 + digit
    return num

s = "12345"
print(type(s))
print("string : ", s)
num = to_number(s)  # Output: 12345
print("number : ", num)
print(type(num))



