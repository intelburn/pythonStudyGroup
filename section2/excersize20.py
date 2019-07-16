def converter(kg, coef=2.20462):
    return kg * coef

a = int(input("Enter the first parameter: "))
second_param = input("Do you want to enter a second parameter (y/N)? ")
if second_param.lower() == 'y':
    b = int(input("Enter the second parameter: "))
    print(converter(a, b))
else:
    print(converter(a))


# print(converter(3))
# print(converter(3, 6))