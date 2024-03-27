number = int(input())
sum = 0

for i in range(100, 1000):
    sum += i if i % number == 0 else 0

print(sum)
