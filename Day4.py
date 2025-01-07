def sum_of_even_numbers(n):
    total_sum = 0
    for number in range(2, n+1, 2):
        total_sum += number
    return total_sum

n = int(input("Enter a positive integer: "))

if n > 0:
    result = sum_of_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
else:
    print("Please enter a positive integer.")
