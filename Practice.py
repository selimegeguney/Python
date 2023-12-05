# def is_it_prime(num):
#     if num < 2 or type(num) != int:
#         return False
#     else:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         return is_prime

# print(is_it_prime(79))

# import math

# def is_it_prime(num):
#     if num < 2 or type(num) != int:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1): #better for optimization
#         if num % i == 0:
#             return False
#     return True

# print(is_it_prime(-4.5))