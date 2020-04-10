# -*- coding: utf-8 -*-       # <= 추가

import os
import sys
import urllib.request
from pygame import mixer
import pygame
import string
import playsound

def has_only_latin_letters(name):
    char_set = string.ascii_letters
    name = name.replace(' ','')
    if all((True if x in char_set else False for x in name)):
        return 'matt'
    else :
        return 'jinho'


def naver_TTS(text):
    client_id = "qg9zow8wko"           # <= 변경
    client_secret = "j9DfzIcHNXnBOfVNHQ4GPYgLeV1I6N20LEBtuC7P" # <= 변경
    encText = urllib.parse.quote(text)
    language = has_only_latin_letters(text)
    data = "speaker={}&speed=-1&text=".format(language) + encText
    url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)

    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        
        response_body = response.read()
        try: 
            with open('sounds/temporary.mp3', 'wb') as f:
                f.write(response_body)
            mixer.init()
            mixer.music.load('sounds/temporary.mp3')
            mixer.music.play()
            while mixer.music.get_busy(): # check if the file is playing
                pass
            pygame.time.wait(100)
            f.close()
            
            #mixer.music.stop()
            #pygame.quit()

            #os.remove('temporary.mp3')
       
        except : 
            print('+')
            with open('sounds/temporary1.mp3', 'wb') as f:
                f.write(response_body)

            mixer.init()
            mixer.music.load('sounds/temporary1.mp3')
            mixer.music.play()
            while mixer.music.get_busy(): # check if the file is playing
                pass

            #mixer.music.stop()
            #pygame.quit()
        
            #os.remove('temporary1.mp3')

    

    else:
        print("Error Code:" + rescode)


if __name__ == '__main__':
    
    for _ in range(1):
        naver_TTS("나는 똑똑한 동은씨의 인공지능 비서, 이지스입니다.")
