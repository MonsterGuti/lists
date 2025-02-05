n = int(input())
positive_list = []
negative_list = []
positive_count = negative_sum = 0
for _ in range(n):
    num = int(input())
    if num >= 0:
        positive_count += 1
        positive_list.append(num)
    else:
        negative_sum += num
        negative_list.append(num)
print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count}\nSum of negatives: (negative_sum)")