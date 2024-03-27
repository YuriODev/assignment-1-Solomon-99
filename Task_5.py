num_of_cars = int(input())
while num_of_cars > 30 or num_of_cars < 1:
    num_of_cars = int(input())

speeds = []

for i in range(num_of_cars):
    speed = int(input())
    speeds.append(speed)

faster_than_60 = "Yes" if max(speeds) > 60 else "No"

average_speed = sum(speeds) / num_of_cars

print(f"{average_speed:.1f}")
print(faster_than_60)