# 게임 아이템 시세 예측을 통한 이상 거래 탐지
개요 : 경매장의 비정상적인 사용으로 인한 게임 재화 생산량의 문제 발생
- 던전앤@@@의 API를 이용한 거래 데이터 수집 및 던@나우의 실시간 인기 검색어 크롤링을 통한 주요 아이템 선정
- 역할 : API를 이용한 크롤링, 웹사이트 크롤링, 전처리
  
- 파이캐럿과 챗봇(gradio)에 대해 학습함.
- 시계열 데이터을 학습에 이용하기 위한 전처리를 학습함.
- 특정 단어와 가장 유사한 단어를 불러오기 위해 difflib의 get_close_matches를 사용함.
  
모델 선정 기준(파이캐럿)

![image](https://github.com/Mokhwa96/First-Team-Project/assets/149074033/a1c66e00-af3d-4307-9d06-886ba193b729)

챗봇(gradio)

![image](https://github.com/Mokhwa96/First-Team-Project/assets/149074033/5a9bdf75-4b4a-4c4a-9e64-1ef847ace269)

이상 거래 판단 기준

![image](https://github.com/Mokhwa96/First-Team-Project/assets/149074033/4475a47a-660f-4f4f-b752-58b1345fcdc4)

예측 결과

![image](https://github.com/Mokhwa96/First-Team-Project/assets/149074033/6044323c-6df6-4e21-aa80-b434e63e32c6)
