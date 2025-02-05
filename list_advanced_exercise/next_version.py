user_version = input().split(".")
integers_version = list(map(int, user_version))

for index in range(len(integers_version) - 1, -1, -1):
    if integers_version[index] == 9:
        if integers_version[index - 1] == 9:
            integers_version[index - 2] += 1
            integers_version[index] = integers_version[index - 1] = 0
            break
        else:
            integers_version[index] = 0
            integers_version[index - 1] += 1
            break
    else:
        integers_version[2] += 1
        break

string_version = ".".join(map(str, integers_version))
print(string_version)
