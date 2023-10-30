import os
os.chdir("G:/.shortcut-targets-by-id/1rlRbTHMt0NUEyP8qWoMFBsBO1r3KNnsD/[광인사] 1차 프로젝트/던파/0801_new")

import pandas as pd
import requests
import json
import time
from datetime import datetime
import pytz

korea_timezone = pytz.timezone('Asia/Seoul')

items_name = [
    '광명의 루멘',
    '한기',
    '무결점 골든 베릴',
    '시브의 보조장비 보주',
    '왜곡된 차원의 큐브[교환가능]',
    '진정한 각성을 이룬 자',
    '초전도 에너지 코어 상자[1회 교환가능]',
    '백룡의 뿔',
    '균열의 단편',
    '무결점 라이언 코어',
    '무결점 조화의 결정체',
    '견고한 수호자의 모래시계',
    '수호자의 모래시계',
    '기민한 흑룡의 날개',
    '차오르는 수호자의 망토',
    '눈부신 황혼의 공명',
    '차오르는 수호자의 모래시계',
    '날카로운 흑룡의 날개',
    '기운찬 적룡의 뿔',
    '기운찬 백룡의 뿔',
    '황금빛 황혼의 공명',
    '조화로운 흑룡의 뿔',
    '조화로운 적룡의 뿔',
    '조화로운 백룡의 뿔',
    '기민한 적룡의 날개',
    '칠흑같은 황혼의 공명',
    '조화로운 청룡의 뿔',
    '기운찬 청룡의 뿔',
    '빛을 머금은 이슬',
    '기운찬 흑룡의 뿔',
    '기민한 백룡의 날개',
    '날카로운 청룡의 날개',
    '날카로운 적룡의 날개',
    '조화로운 황룡의 뿔',
    '기민한 청룡의 날개',
    '타오르는 영원의 달빛',
    '기운찬 황룡의 뿔',
    '날카로운 백룡의 날개',
    '기운찬 비룡의 갈기',
    '타오르는 황혼의 공명',
    '비룡의 기운찬 발톱',
    '비룡의 기운찬 비늘',
    '태양을 삼킨 달',
    '맹렬한 비룡의 심장',
    '거룩한 저주의 서',
    '비룡의 단단한 발톱',
    '축제의 여왕 페리아 알',
    '워터밤 페스타 아바타[시크릿] 풀세트 상자[여자]',
    '페스타의 추억 칭호 상자'
]
while True:
    for item_name in items_name:
        now = datetime.now(korea_timezone)
        key = 'EUw0kZ4YcWiVWURf9f9DtfwW3p8gbF0x'
        url = f'https://api.neople.co.kr/df/auction-sold?itemName={item_name}&limit=100&apikey={key}'
        response = requests.get(url)
        contents = response.text
        data = json.loads(contents)
        df = pd.DataFrame(data['rows'])
        df.to_csv(f'{now.month}_{now.day}_{now.hour}_{item_name}_data.csv', index=False)
        time.sleep(1)
    time.sleep(3600)
