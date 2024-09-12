import json
import threading
import requests
from concurrent.futures import ThreadPoolExecutor


green_light_red_light = threading.Lock()

results = []

def get_post(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with green_light_red_light:
            results.append(data)


def main():
    with ThreadPoolExecutor(max_workers = 11) as executor:
        executor.map(get_post, range(1,78))

    with green_light_red_light:
        with open('data.json', 'w') as f:
            json.dump(results, f, indent = 4)



if __name__ == '__main__':
    main()

