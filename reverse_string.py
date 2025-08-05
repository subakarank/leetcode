
def reverse_string(s: list) -> list: 
    reverse = []
    for i in range(len(s)-1, -1, -1 ):
        reverse.append(s[i])
    return reverse

s = ["h","e","l","l","o"]
print(s)
print(reverse_string(s))

def reverse_string_optimised(s: list) -> list: 
    left, right  = 0 , len(s) - 1 
 
    while left < right:
        s[left], s[right] = s[right], s[left] 
        left += 1 
        right -= 1
    return s   

s = ["h","e","l","l","o"]

print("reverse_string_optimised", reverse_string_optimised(s))



