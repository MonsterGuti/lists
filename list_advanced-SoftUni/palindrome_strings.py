user_input = input().split()
user_word = input()
palindrome_count = 0
palindrome_list = []
for word in user_input:
    if word == word[::-1]:
        palindrome_list.append(word)
        if word == user_word:
            palindrome_count += 1
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")

