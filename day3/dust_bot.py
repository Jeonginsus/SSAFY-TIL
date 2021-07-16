from typing import Awaitable
import requests

TOKEN = '1897928248:AAGwwpUsHoMFuL4Yl05nP6GUxkhBAJCP4Mw'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()


chat_id = response.get('result')[-1].get('message').get('chat').get('id')
message = response.get('result')[-1].get('message').get('text')

if(message == '미세먼지'):

    key='n1oe5Xa6Q7bwfgqDDQ2p2wILottz25R2BfrU1y4azlCrfHyFI6jxli1Ms4VDbDC%2Bg%2F323Ti7yw%2BCwSWP867khg%3D%3D'

    locate = '부산'

    url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={locate}&returnType=json'

    response = requests.get(url).json()

    # print(response['response']['body']['items'][1]['pm10Value'])
    text = ''
    for a in range(len(response['response']['body']['items'])):
        loc = response['response']['body']['items'][a]['stationName']
        mise = response['response']['body']['items'][a]['pm10Value']
        text = text + f'현재 {locate} {loc}의 미세먼지 농도는 {mise}입니다.\n'
        print(text)
    message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)