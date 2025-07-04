def is_prime():
    num = int(input("Enter a number to check if it's prime: "))
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


snt = is_prime()

print(f"{snt} is {'a prime number' if snt else 'not a prime number'}")