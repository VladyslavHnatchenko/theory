import requests


r = requests.get('https://google.com')


if r.status_code == 200:
    print('All right!')

if r.status_code == 404:
    print("Page not found!")
