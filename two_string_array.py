
def two_string_array(word1: list[str], word2: list[str]):
    word1_string = ''
    word2_string = ''
    for word in word1:
        word1_string += word

    for word in word2:
        word2_string += word
    
    return word1_string == word2_string

print(f'word1 = ["ab", "c"], word2 = ["a", "bc"] output: True {two_string_array(["ab", "c"], ["a", "bc"])}' )
print(f'Input: word1 = ["a", "cb"], word2 = ["ab", "c"] output: False {two_string_array(["a", "cb"], ["ab", "c"])}')

def two_string_array_1(word1: list[str], word2: list[str]):
   
    word1_string = ''.join([word for word in word1])
    word2_string = ''.join([word for word in word2])

    return word1_string == word2_string

print(f'word1 = ["ab", "c"], word2 = ["a", "bc"] output: True {two_string_array_1(["ab", "c"], ["a", "bc"])}' )
print(f'Input: word1 = ["a", "cb"], word2 = ["ab", "c"] output: False {two_string_array_1(["a", "cb"], ["ab", "c"])}')

def two_string_array_2(word1: list[str], word2: list[str]):
   
    return ''.join(word1) == ''.join(word2)

print(f'word1 = ["ab", "c"], word2 = ["a", "bc"] output: True {two_string_array_2(["ab", "c"], ["a", "bc"])}' )
print(f'Input: word1 = ["a", "cb"], word2 = ["ab", "c"] output: False {two_string_array_2(["a", "cb"], ["ab", "c"])}')   