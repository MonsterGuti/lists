user_string = input().split()
filtered_list = []
for word in user_string:
    digit_chars = ""
    len_of_digits = 0
    for char in word:
        if char.isdigit():
            digit_chars += char
            len_of_digits += 1
    word = chr(int(digit_chars)) + word[len_of_digits:]
    char_list = [char for char in word]
    char_list[1], char_list[-1] = char_list[-1], char_list[1]
    final_word = "".join(char_list)
    filtered_list.append(final_word)
    char_list = []

print(" ".join(filtered_list))
