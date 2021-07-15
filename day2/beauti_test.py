import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

dollar = data.select_one('.usd>.head_info>.value')
result = dollar.text
# print(result)

print(f'현재의 달러환율은 {result}입니다.')