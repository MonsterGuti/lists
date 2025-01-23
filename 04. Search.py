n = int(input())
word = input()
my_list = []
for i in range(n):
    sentence = input()
    my_list.append(sentence)
print(my_list)
for j in range(len(my_list) - 1, -1, -1):
    element = my_list[j]
    if word not in element:
        my_list.pop(j)
print(my_list)