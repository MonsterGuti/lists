notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    priority = int(command[0]) - 1
    action = command[1]
    notes.pop(priority)
    notes.insert(priority, action)
for note in range(len(notes) - 1, -1, -1):
    if notes[note] == 0:
        notes.pop(note)
print(notes)
