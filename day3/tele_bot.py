from typing import Awaitable
import requests

TOKEN = '1897928248:AAGwwpUsHoMFuL4Yl05nP6GUxkhBAJCP4Mw'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

#응답 내용 저장하기
update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id 뽑아내기

chat_id = response.get('result')[0].get('message').get('chat').get('id')

print(chat_id)
### 메시지를 보내보자..
#필수 조건
# 1. chat_id
# 2. text

# text = '승훈님 별다방 아메리카노 당첨!'

# message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

# requests.get(message_url)