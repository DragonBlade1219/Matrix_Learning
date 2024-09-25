def shifted_vowels(word: str) -> str:

    vowels = "aeiou"
    chars_temp = []
    word = list(word)
    
    for i in range(len(word)):
        if word[i] in vowels:
            if len(chars_temp) == 0:
                chars_temp.append(word[i])
                first_position = i
                continue
            chars_temp = [word[i]] + chars_temp
            word[i] = chars_temp.pop()
        elif len(chars_temp) == 0 and i == len(chars_temp) - 1:
            return word
    if  len(chars_temp) != 0:  
        word[first_position] = chars_temp.pop()
        
    return ''.join(word)
    
    # word_shifted = word
    
    # for i in range (len(word_shifted)):
    #     if word_shifted[i] in vowels and i != (len(word_shifted) - 1):
    #         word_shifted[i] = chars_temp[i+1][1]
    #     elif i == (len(word_shifted) - 1):
    #         word_shifted[i] = chars_temp[0][1]
    
    # return ''.join(word_shifted)
                
        