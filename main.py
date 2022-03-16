import requests
from bs4 import BeautifulSoup


def parser(word):
    url = 'https://context.reverso.net/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/' \
          '%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-' \
          '%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9/' + word
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 '
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    if response.status_code == 200:
        items_pm = soup.findAll('div', class_='wide-container', id='translations-content')
        comps_pm = []
        for item_pm in items_pm:
            comps_pm.append(item_pm.get_text(', ', strip=True, ))
        for comp_pm in comps_pm:
            print('Translate:', comp_pm, '\n')
        items = soup.findAll('div', class_='src ltr')
        items_v = soup.findAll('div', class_='trg ltr')
        comps = []
        comps_translate = []
        for item in items:
            comps.append(item.get_text(' ', strip=True, ))
        for item_v in items_v:
            comps_translate.append(item_v.get_text(' ', strip=True, ))
        print('Pattern:')
        for i in range(len(comps)):
            print(comps[i])
            print(comps_translate[i], '\n')
    else:
        print("Error! Unable to connect to the site!")


try:
    word = str(input('Input word: '))
    assert len(word) != 0
    parser(word)
except(ValueError, AssertionError):
    print('Input word for translation!')