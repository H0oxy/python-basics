lesson_dates = ['19.05.15',
                 '19.05.17',
                 '19.05.18',
                 '19.05.19',
                 '19.05.20',
]

student_marks = [5,
                 4,
                 3,
                 2,
                 5
]

# lesson_dates_and_marks = [
#                 ['19.05.15', 5],
#                 ['19.05.17', 4],
#                 ['19.05.18', 3],
#                 ['19.05.19', 2],
#                 ['19.05.20', 5],
# ]

# i = 0
# while i < len(student_marks):
#     print(lesson_dates[i], 'оценка', student_marks[i])
#     i += 1

# print('оценка', mark)
# for mark in student_marks:

# print('оценка', mark)
# for item in enumerate(student_marks, 1): # pairs->(num, item)
#     print('оценка', item)

# user_full_name = ['Ivan', 'Ivanov']
# first_name = user_full_name[0]
# second_name = user_full_name[1]
# print(first_name, second_name)
#

# for i, item in enumerate(student_marks): # pairs->(num, item)
#     print('оценка', i, item)
#     print(lesson_dates[i], 'оценка', mark)

for record in lesson_dates_and_marks:
    lesson_dates, mark = record
    print(lesson_dates, 'оценка', mark)

for lesson_dates, mark in lesson_dates_and_marks:
    print(lesson_dates, 'оценка', mark)


for lesson_dates, mark id zip(lesson_dates, student_marks): # ['19.05.15', 5]
    print(lesson_dates, 'оценка', mark)