# my_id = {'name': 'Selim', 'age': 19, 'number': 1234567890, 'email': 'example@example.com'}
# print(my_id)

# for key in my_id.keys():
#     print(key)
# print('*****')

# for value in my_id.values():
#     print(value)
# print('*****')

# for item in my_id.items():
#     print('The', item[0], 'is', item[1])
# print('*****')

# for key, value in my_id.items():
#     print('The', key, 'is', value)


# print("***************")

classroom = {'34496': {'name': 'Selim', 'age': 19, 'number':'34496'}, '34532': {'name': 'Duha', 'age': 18}, '34550': {'name': 'Bahadır', 'age': 19}}

for student_number, information in classroom.items():
    print('The student number is', student_number)
    for info_key, info_value in information.items():
        print('The', info_key, 'is', info_value)
    print('\n*****\n')

classroom['teachers'] = ['Piotr', 'Peter', 'Pierre']

print(classroom['teachers'][0])

my_id = {'name': 'Selim', 'age': 19, 'number': 1234567890, 'email': 'example@example.com', 'favourite cars': ['BMW', 'Mercedes', 'Audi']}

print('\n*********\n')

for key, value in my_id.items():
    if (type(value)==str):
        print('My', key, 'is', value)
    if (type(value)==list):
        print('My', key, 'are', ', '.join(value))



