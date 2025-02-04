string_of_integers = input().split(", ")
beggars_count = int(input())
money_as_integers = []
for money in string_of_integers:
    money_as_integers.append(int(money))
beggars_sum = []
start_index = 0
for current_beggar in range(beggars_count):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_integers), beggars_count):
        current_beggar_sum += money_as_integers[index]
    beggars_sum.append(current_beggar_sum)
    start_index += 1
print(beggars_sum)