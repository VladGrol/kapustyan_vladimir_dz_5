from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']

result = zip_longest(tutors, classes)

print(result)  # докзываем, что zip_longest - это генератор
print(*result)
print(next(result))
