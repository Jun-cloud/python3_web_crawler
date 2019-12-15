import requests
from bs4 import BeautifulSoup

MEMBER_DATA = {
    'memberID' : 'a'
    , 'memberPassword' : 'a'
}

# 하나의 세션(Session) 객체를 생성해 일시적으로 유지합니다.
with requests.Session() as s:
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp', data=MEMBER_DATA)

print(request.text)
