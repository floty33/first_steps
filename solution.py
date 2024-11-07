def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

with open('in_nums.txt', 'r') as infile:
    numbers = [int(line.strip()) for line in infile]

results = []
for number in numbers:
    if is_prime(number):
        last_digit = number % 10
        fib_number = fibonacci(last_digit)
        results.append(str(fib_number))

with open('out_nums.txt', 'w') as outfile:
    outfile.write("\n".join(results))
