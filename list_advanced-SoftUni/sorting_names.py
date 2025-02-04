names_string = input().split(", ")
sorted_name_list = sorted(names_string, key=lambda x: (-len(names_string), x))
print(sorted_name_list)