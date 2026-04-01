# day1_requests_example.py
# 이 파일은 터미널에서 python day1_requests_example.py 로 실행합니다
#
# [실습 순서]
# 1. 가상환경 활성화 후, requests 설치 전에 실행 → ModuleNotFoundError 확인
# 2. pip install requests 로 설치
# 3. 다시 실행 → 정상 동작 확인

import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()

print("응답 데이터:", data)
print("고양이 사실:", data["fact"])
