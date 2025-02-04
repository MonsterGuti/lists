user_text = input()
new_word = ""
for char in user_text:
    if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
        new_word += char
print(new_word)
