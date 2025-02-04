happiness_list = list(map(int, input().split()))
happiness_factor = int(input())
employees_count = len(happiness_list)
average_value = sum(happiness_list) / employees_count
filtered_happiness_list = list(filter(lambda x: x >= average_value, happiness_list))
if len(filtered_happiness_list) >= employees_count / 2:
    print(f"Score: {len(filtered_happiness_list)}/{employees_count}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happiness_list)}/{employees_count}. Employees are not happy!")