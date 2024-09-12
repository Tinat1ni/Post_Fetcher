import json
import threading
import requests
from concurrent.futures import ThreadPoolExecutor


green_light_red_light = threading.Lock()

def get_post(post_id, file):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with green_light_red_light:
            with open(file, 'a') as f:
                if f.tell() == 0:
                    f.write('[')
                else:
                    f.write(', ')
                json.dump(data, f, indent = 4)


def main():
    file = 'data.json'
    with open(file, 'w') as f:
        f.write('')

    with ThreadPoolExecutor(max_workers=11) as executor:
        executor.map(lambda post_id: get_post(post_id, file), range(1, 78))

    with open(file, 'a') as f:
        f.write(']')


if __name__ == '__main__':
    main()

