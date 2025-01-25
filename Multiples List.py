factor = int(input())
count = int(input())
num_list = []
num = factor
for i in range(count):
    num_list.append(num)
    num += factor
print(num_list)