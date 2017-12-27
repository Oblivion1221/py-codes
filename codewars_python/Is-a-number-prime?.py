def is_prime(num):
    if num < 2:
        return False
    is_prime = 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = 0
    return True if is_prime == 1 else False