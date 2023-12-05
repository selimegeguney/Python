def is_it_prime(num):
    if num < 2 or type(num) != int:
        return False
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        return is_prime

print(is_it_prime(79))