import requests

for i in range(1, 6):
    #в цикле изменяем коенчный uri для запроса первых пяти /posts
    tmp_url = 'https://jsonplaceholder.typicode.com/posts/' + str(i)
    #преобразуем ответ в json
    tmp_response = requests.get(tmp_url).json()
    #в цикле выводим все заголовки ответа
    for header_ in tmp_response:
        print(f'"{header_}": {tmp_response[header_]}')
    print()