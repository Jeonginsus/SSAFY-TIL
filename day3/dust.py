import requests


key='n1oe5Xa6Q7bwfgqDDQ2p2wILottz25R2BfrU1y4azlCrfHyFI6jxli1Ms4VDbDC%2Bg%2F323Ti7yw%2BCwSWP867khg%3D%3D'

locate = '부산'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={locate}&returnType=json'

response = requests.get(url).json()

# print(response['response']['body']['items'][1]['pm10Value'])

for a in range(len(response['response']['body']['items'])):
    loc = response['response']['body']['items'][a]['stationName']
    mise = response['response']['body']['items'][a]['pm10Value']
    print(f'현재 {locate} {loc}의 미세먼지 농도는 {mise}입니다.')