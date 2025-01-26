times_string = input().split()
finish_line = len(times_string) // 2
left_car = times_string[:finish_line]
right_car = times_string[-1:finish_line:-1]
left_car_sum = right_car_sum = 0

for time in left_car:
    if int(time) == 0:
        left_car_sum *= 0.8
    if int(time) != 0:
        left_car_sum += int(time)

for time in right_car:
    if int(time) == 0:
        right_car_sum *= 0.8
    if int(time) != 0:
        right_car_sum += int(time)

if left_car_sum < right_car_sum:
    print(f"The winner is left with total time: {(left_car_sum):.1f}")
elif left_car_sum > right_car_sum:
    print(f"The winner is right with total time: {(right_car_sum):.1f}")
else:
    print(f"Draw! Total time: {(right_car_sum):.1f}")
