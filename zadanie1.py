import requests

for i in range(1, 6):
    tmp_url = 'https://jsonplaceholder.typicode.com/posts/' + str(i)
    tmp_response = requests.get(tmp_url).json()
    for header_ in tmp_response:
        print(f'"{header_}": {tmp_response[header_]}')
    print()