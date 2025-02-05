scientist_input = int(input())
electrons_list = []

for index in range(scientist_input):
    electrons_list.append(2 * (index + 1) ** 2)
    index += 1
    if sum(electrons_list) == scientist_input:
        break
    if sum(electrons_list) > scientist_input:
        electrons_list.pop()
        electrons_list.append(scientist_input - sum(electrons_list))
        break

print(electrons_list)
