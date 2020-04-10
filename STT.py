import sys
import requests
from datetime import datetime

def naver_STT(filename):
    client_id = "qg9zow8wko"
    client_secret = "j9DfzIcHNXnBOfVNHQ4GPYgLeV1I6N20LEBtuC7P"
    lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = open(filename, 'rb')
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url,  data=data, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        

        return response.text
    else:
        return ("Error : " + response.text)

if __name__ == "__main__":
    print(naver_STT('sounds/temporary.mp3'))