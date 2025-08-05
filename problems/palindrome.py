'''A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

- convert to lowercase 
- remove non alpha numeric 
- reverse and then compare 

'''
def palindrome(s: str) -> bool:
    new_string = ''.join([char.lower() for char in s if char.isalnum()])
    return  new_string == new_string[::-1]

    # string_list = []
    # for char in s: 
    #     if char.isalnum():
    #         string_list.append(char.lower())
    # new_string = ''.join(string_list)
    # print("new string before reverse", new_string)
    # reverse_string = new_string[::-1]
    # print("reverse string ", reverse_string)
    # if new_string == reverse_string:
    #     return True
    # else:
    #     return False
    

print("is palindrome?:", palindrome('A man, a plan, a canal: Panama'))



