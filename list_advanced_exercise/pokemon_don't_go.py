sequence_of_integers = [int(num) for num in input().split()]
sum_of_removed = 0

while sequence_of_integers:
    index = int(input())

    if index < 0:
        removed_value = sequence_of_integers[0]
        sequence_of_integers[0] = sequence_of_integers[-1]
    elif index >= len(sequence_of_integers):
        removed_value = sequence_of_integers[-1]
        sequence_of_integers[-1] = sequence_of_integers[0]
    else:
        removed_value = sequence_of_integers.pop(index)

    sum_of_removed += removed_value

    for i in range(len(sequence_of_integers)):
        if sequence_of_integers[i] <= removed_value:
            sequence_of_integers[i] += removed_value
        else:
            sequence_of_integers[i] -= removed_value

print(sum_of_removed)
