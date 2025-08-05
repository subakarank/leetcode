'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

'''
'''
step 1 : check character availabilty 
step 2: count check 
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

# Remove one character from a string
def remove_char(s, index):
    if index < 0 or index >= len(s):
        raise ValueError("Index out of range")
    return s[:index] + s[index+1:]

# Reverse a string without slicing
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
        print(reversed_str)
    return reversed_str

# Test the functions
original = "hello"
index_to_remove = 1  # Remove the second character (index 1, 'e')

# Remove character
result_remove = remove_char(original, index_to_remove)
print(f"String after removing index {index_to_remove}: {result_remove}")

# Reverse string
result_reverse = reverse_string(original)
print(f"Reversed string: {result_reverse}")



# def without_counter(magazine: str, ransome_note: str) -> bool:
#     magazine_count = {}
#     ransome_note_count = {}
#     for char in magazine:
#         magazine_count[char] = magazine_count.get(char, 0) + 1 

#     for char in ransome_note:
#         ransome_note_count[char] = ransome_note_count.get(char, 0) + 1 
#     print("magazine_count", magazine_count)
#     print("ransome_note_count", ransome_note_count)

#     for char in ransome_note_count: 
#         if char not in magazine_count:
#             return False
#         elif magazine_count[char] < ransome_note_count[char]:
#             return False 
        
#     return True
# from collections import Counter
# def with_counter(magazine: str, ransome_note: str) -> bool:
#     magazine_count = Counter(magazine)
#     ransome_note_count = Counter(ransome_note)
    
#     print("magazine_count", magazine_count)
#     print("ransome_note_count", ransome_note_count)

#     for char in ransome_note_count: 
#         if char not in magazine_count:
#             return False
#         elif magazine_count[char] < ransome_note_count[char]:
#             return False 
        
#     return True

# print("without_counter", without_counter('aab' , 'aa')) 
# print("with_counter", with_counter('aab' , 'aa')) 