lesson_dates = [
                 '19.05.15',
                 '19.05.17',
                 '19.05.18',
                 '19.05.19',
                 '19.05.20',
]

student_marks = [
                 5,
                 4,
                 3,
                 2,
                 5
]

student_marks_2 = [
                 4,
                 3,
                 5,
                 5,
                 3
]

for lesson_dates, mark, mark_2 in zip(lesson_dates, student_marks, student_marks_2): # ['19.05.15', 5, 4]
    print(lesson_dates, 'оценка', mark, mark_2)
