lst = input().split()
lst = [int(x) for x in lst]

while True:
    command = input()

    if command == "end":
        print("[", end="")
        for i in range(len(lst)):
            if i != 0:
                print(", ", end="")
            print(lst[i], end="")
        print("]")
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "exchange":
        index = int(command_parts[1])
        if 0 <= index < len(lst):
            lst = lst[index + 1:] + lst[:index + 1]
        else:
            print("Invalid index")

    elif action == "max":
        type_of_value = command_parts[1]
        if type_of_value == "even":
            max_even_value = -1
            max_even_index = -1
            for i in range(len(lst)):
                if lst[i] % 2 == 0 and lst[i] >= max_even_value:
                    max_even_value = lst[i]
                    max_even_index = i
            if max_even_index == -1:
                print("No matches")
            else:
                print(max_even_index)
        elif type_of_value == "odd":
            max_odd_value = -1
            max_odd_index = -1
            for i in range(len(lst)):
                if lst[i] % 2 != 0 and lst[i] >= max_odd_value:
                    max_odd_value = lst[i]
                    max_odd_index = i
            if max_odd_index == -1:
                print("No matches")
            else:
                print(max_odd_index)

    elif action == "min":
        type_of_value = command_parts[1]
        if type_of_value == "even":
            min_even_value = None
            min_even_index = -1
            for i in range(len(lst)):
                if lst[i] % 2 == 0:
                    if min_even_value is None or lst[i] < min_even_value:
                        min_even_value = lst[i]
                        min_even_index = i
            if min_even_value is None:
                print("No matches")
            else:
                print(min_even_index)

        elif type_of_value == "odd":
            min_odd_value = None
            min_odd_index = -1
            for i in range(len(lst)):
                if lst[i] % 2 != 0:
                    if min_odd_value is None or lst[i] < min_odd_value:
                        min_odd_value = lst[i]
                        min_odd_index = i
            if min_odd_value is None:
                print("No matches")
            else:
                print(min_odd_index)


    elif action == "first":
        count = int(command_parts[1])
        type_of_value = command_parts[2]
        if count > len(lst):
            print("Invalid count")
        else:
            result = []
            if type_of_value == "even":
                for num in lst:
                    if num % 2 == 0:
                        result.append(num)
                    if len(result) == count:
                        break
            else:
                for num in lst:
                    if num % 2 != 0:
                        result.append(num)
                    if len(result) == count:
                        break
            if len(result) == 0:
                print("[]")
            else:
                print(result)

    elif action == "last":
        count = int(command_parts[1])
        type_of_value = command_parts[2]
        if count > len(lst):
            print("Invalid count")
        else:
            result = []
            if type_of_value == "even":
                for num in reversed(lst):
                    if num % 2 == 0:
                        result.append(num)
                    if len(result) == count:
                        break
            else:
                for num in reversed(lst):
                    if num % 2 != 0:
                        result.append(num)
                    if len(result) == count:
                        break
            if len(result) == 0:
                print("[]")
            else:
                print(result[::-1])
