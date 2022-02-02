import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = (zip(tutors,klasses) if len(tutors) < len(klasses) else itertools.zip_longest(tutors,klasses))
for i in gen:
    print(*gen)

print("Генератор истощен (((",*gen,"- должен быть генератор")