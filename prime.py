# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Print prime numbers from 1 to 10
for num in range(1, 11):
    if is_prime(num):
        print(num)

