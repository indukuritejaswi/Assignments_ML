##1
n = int(input())

for i in range(1, n + 1):
    print(i)

sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1

print(sum_numbers)

##2
def calculate_square(n):
    return n * n

n = int(input())

result = calculate_square(n)
print(result)
