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

for lesson_dates, mark id zip(lesson_dates, student_marks): # ['19.05.15', 5]
    print(lesson_dates, 'оценка', mark)

# student_marks = []
# while True:
#        mark = input('введите оценку студента:\n')
#        if mark:                           # '' == False, () == False, [] == False
#            student_marks.append(int(mark))
#        else:
#          break
#
# print('ввод завершен')
# print(student_marks)

#mock_student_marks = ['5', '4', '3', '2']
mock_student_marks = [5, 4, 3, 2]
student_marks = mock_student_marks

#i = 0
avg_mark = 0
for item in student_marks:
    avg_mark += item

#while i < len(student_marks):
   # print(type(avg_mark), type(student_marks[i]))
    #avg_mark += int(student_marks[i])
    #i += 1
for mark in enumerate(student_marks):
    print('оценка', mark)

user_full_name = ['Ivan, Ivanov']
first_name, second_name = user_full_name

print(first_name, second_name)
a, b, c, d, e = [15, 45, 87, 96, 4]
print (a, b, c, d, e)

mock_student_marks = [5,4,3,2,5]
#print(dir(mock_student_marks))

print(mock_student_marks)
mock_student_marks.append(5)
print(mock_student_marks)
# print(mock_student_marks.index(5, 1))
# print(mock_student_marks.index(5, 5))
# print(mock_student_marks.index(5, 1, 5))

num = 2
if mock_student_marks.count(num) :
    print (num, 'found', mock_student_marks.count(num), 'times, first index', mock_student_marks.index(num))
else:
    print(num, 'not found')

# print ('5 count', mock_student_marks.count(5))
# print ('2 count', mock_student_marks.count(2))
# # print (mock_student_marks.index(15))
# if mock_student_marks.count(15) :
#     print('15 index', mock_student_marks.index(15))
# if mock_student_marks.count(5) :
#     print('5 index', mock_student_marks.index(5))

# i = 0
# while i < len(student_marks) :
#     print(mock_lesson_dates[i],'mark', student_marks[i])
#     i += 1
# for item in student_marks:
#     print('оценка', item)
#
# for item in enumerate(student_marks):
#     print('оценка', item)
#
#
#
# for lesson_date, mark in lesson_dates_and_marks:
#     #print(mock_lesson_dates[i],'оценка', mark)
#     #lesson_dates, mark = record
#     print (lesson_dates, 'оценка', mark)
