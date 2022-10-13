from bs4 import BeautifulSoup
import pandas
import requests

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

params = {
    'serviceKey': 'LK5HxMQO7ScyFpgYc6+QgNRsqPfAKmnW1fczw8kHYE4BDXCaUX7uBUrZXK6wXoDnS5vivk2h0fYiboTWVjRjvQ==',
    'returnType': 'xml',
    'numOfRows': '10',
    'pageNo': '1',
    'stationName': '주안',
    'dataTerm': 'DAILY',
    'ver': '1.0'
}

response = requests.get(url, params=params)
# print(response.content)

soup = BeautifulSoup(response.text, 'html.parser')
ItemList = soup.findAll('item')

data = list

for item in ItemList:

    # print(item)
    print('측정소: 주안')
    print('pm25Value: ' + item.find('pm25value').text)
    print('dataTime: ' + str(item.find('datatime').text))
    print("-------")