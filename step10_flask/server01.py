from urllib.parse import urlencode
import requests
from urllib.request import urlopen, Request
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

# url = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
# response = requests.get(url)
# print(response.content)

# 공공 데이터
# url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
# params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
# response = requests.get(url, params=params)
# print(response.content)

# 서비스키 (Decoding)
# BduNCP5EEbI5qrcJOJzv1R17qojDBm/tgyTAMsfmKkCesE0yi9n0fb7bf2mm2yqRmFy9NFihLXD29SUUlWDCGA==

# 공공 데이터를 받아서 화면에 표 출력하기
url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerStatus'
params = '?' +urlencode({'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'period' : '5', 'zcode' : '11' })
request = Request(url + params)
response_body = urlopen(request).read()
# print(response_body)
# 받은 xml을 DataFrame으로 변경하자
root = ET.fromstring(response_body)
df = pd.DataFrame()

# 이터레이터 즉 item에게 순차적으로 접근할 수 있도록 iter('item')
for item in root.iter('item'):
    # 딕셔너리
    item_dict={}
    item_dict['충전소명'] = (item.find('statNm').text)
    item_dict['주소'] = (item.find('addr').text)
    item_dict['위도'] = (item.find('lat').text)
    item_dict['경도'] = (item.find('lng').text)
    item_dict['충전기상태'] = (item.find('stat').text)
    df = df._append(item_dict, ignore_index=True)

print(df)