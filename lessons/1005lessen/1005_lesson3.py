concrete_request ='https://translate.google.com/?hl=ru#view=home&op=translate&sl=auto&tl=ru&text=patronymic'
# parse GET data -> dict
correct_answer = {
    'view': 'home',
    'op': 'translate',
    'sl': 'en',
    'tl': 'ru',
    'text': 'patronymic',
}
#print(concrete_request)
answer = None

trash,raw_get_data = concrete_request.split('?', maxsplit=1)
print(raw_get_data)
get_data = raw_get_data.split('&')
# print(get_data)


parsed_get_data = []
parsed_get_data_as_dict = {}
for pair in get_data:
    # print(pair.split('='))
    tmp = pair.split('=')
    parsed_get_data.append(tmp)
    parsed_get_data_as_dict[tmp[0]] = tmp[1]
    parsed_get_data.append(pair.split('='))
print(parsed_get_data)
print(parsed_get_data_as_dict)

answer = parsed_get_data_as_dict

# assert anser == correct_answer, 'bad parser!'