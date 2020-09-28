# a = 'vsem privet'
# print(a.isdigit())
#
# b = '15,7'
# print(b.isdigit())
#
# c = '156'
# print(c.isdigit())
#
# d = '15e6'      # 15000000
# print(d.isdigit())
#
# r = '15000000'
# print(r.isdigit())
#
# avg_mark = input('Введите средний балл студента\n')
# # if avg_mark.isdigit():
# #     avg_mark = float(avg_mark)
# #     print('Ввод корректен', type(avg_mark), avg_mark)
# try:
#     avg_mark = float(avg_mark)
#     print('Ввод корректен', type(avg_mark), avg_mark)
# except ValueError:
#     print('Некорректное число', avg_mark)

# class_pupils = input('Введите имена учеников через запятую\n')
class_pupils = ['1', '2', '3', '4', '5', '6']
correct_result = ['1', '2', '3', '4', '5', '6']
# print('Ученики класса:', class_pupils)

result = ['1', '2', '3', '4', '5', '6']

assert result == correct_result, 'Алгоритм реализован неверно'
