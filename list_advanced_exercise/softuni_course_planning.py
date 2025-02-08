lessons_string = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command_parts = command.split(":")
    command_type = command_parts[0]
    lesson_title = command_parts[1]

    if command_type == "Add":
        if lesson_title not in lessons_string:
            lessons_string.append(lesson_title)

    elif command_type == "Insert":
        index = int(command_parts[2])
        if lesson_title not in lessons_string:
            lessons_string.insert(index, lesson_title)

    elif command_type == "Remove":
        if lesson_title in lessons_string:
            lessons_string.remove(lesson_title)
            exercise = f"{lesson_title}-Exercise"
            if exercise in lessons_string:
                lessons_string.remove(exercise)

    elif command_type == "Swap":
        lesson_title_2 = command_parts[2]
        if lesson_title in lessons_string and lesson_title_2 in lessons_string:
            index_1, index_2 = lessons_string.index(lesson_title), lessons_string.index(lesson_title_2)
            lessons_string[index_1], lessons_string[index_2] = lessons_string[index_2], lessons_string[index_1]
            exercise_1, exercise_2 = f"{lesson_title}-Exercise", f"{lesson_title_2}-Exercise"
            if exercise_1 in lessons_string:
                lessons_string.remove(exercise_1)
                lessons_string.insert(index_2 + 1, exercise_1)
            if exercise_2 in lessons_string:
                lessons_string.remove(exercise_2)
                lessons_string.insert(index_1 + 1, exercise_2)

    elif command_type == "Exercise":
        exercise = f"{lesson_title}-Exercise"
        if lesson_title in lessons_string:
            if exercise not in lessons_string:
                lesson_index = lessons_string.index(lesson_title)
                lessons_string.insert(lesson_index + 1, exercise)
        else:
            lessons_string.append(lesson_title)
            lessons_string.append(exercise)

for i in range(len(lessons_string)):
    print(f"{i + 1}.{lessons_string[i]}")
