string_of_numbers = input().split()
some_text = input()
some_text_list = []
for char in some_text:
    some_text_list.append(char)

message = ""

for char_number in string_of_numbers:
    index = 0
    for num in char_number:
        index += int(num)

    if index >= len(some_text_list):
        index -= len(some_text_list)

    message += some_text_list.pop(index)

print(message)
