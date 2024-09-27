def remove_special_chars(str):
    res = ''
    for char in str:
        if char.isalnum():
            res += char
    return res

def word_count_in_array(word, array):
    count = 0
    for current_word in array:
        if word.lower() == current_word.lower():
            count += 1
    return count

words = input().split()
words = [remove_special_chars(word) for word in words]

[print(f'{word} -> {word_count_in_array(word, words)}') for word in words]