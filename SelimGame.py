point = 0
questions_ = {'When did Istanbul conquered':'1453','What is the Capital of Poland (English and capital first letter please)':'Warsaw'}
questions = [{'question': 'When did Istanbul conquered', 'answer':'1453','points':10},{'question':'What is the Capital of Poland', 'answer':'Warsaw', 'points': 5, 'warning':'English and capital first letter please'}]

for element in questions:
    answer = input(element['question'])
    if answer == element['answer']:
        print('Correct')
        point += element['points']
        print('Your Point is:', point)
        print('*****')
        
    else:
        print('Wrong! The answer is',element['answer'])
        point -= element['points']/2
        print('Your Point is:', point)
        print('*****')
print('Final point is:', point)
