sequence_of_numbers = list(map(int, input().split(", ")))
group_max = 10
while sequence_of_numbers:
    group = [num for num in sequence_of_numbers if num <= group_max]
    sequence_of_numbers = [num for num in sequence_of_numbers if num > group_max]
    print(f"Group of {group_max}'s: {group}")
    group_max += 10