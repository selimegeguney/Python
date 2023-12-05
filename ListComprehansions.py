print([2*x for x in range(1,11)])


# list(2**x for x in range(1,11))

# [2**x for x in range(1,11)]

temperatures_fahrenheit = [67, 70, 74, 75, 72, 72, 73, 68, 65, 69, 70, 71, 74, 76, 77, 78, 70, 72, 68, 65, 66, 71, 74, 76, 75, 77, 79, 80, 81, 82]
temperatures_celsius  = [(f - 32) * 5/9 for f in temperatures_fahrenheit]

print(temperatures_celsius)


lst = [x for x in [x for x in range(1, 31) if x % 2 == 0] if x % 3 == 0]


print(lst)




