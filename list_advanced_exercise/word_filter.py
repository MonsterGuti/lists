user_text = input().split()
filtered_list = list(x for x in user_text if len(x) % 2 == 0)
print("\n".join(filtered_list))

