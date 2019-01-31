# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = ""
API_KEY = ""


def getHeader():
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header

def getBody(text):
    data = {'text': text}
    return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

def tts(text):
    r = requests.post(URL, headers=getHeader(), data=getBody(text))

    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        if AUE == "raw":
            writeFile("audio/" + "xiaoyan.wav", r.content)
        else:
            writeFile("xiaoyan.mp3", r.content)
    else:
        print(r.text)


if __name__ == '__main__':
    text = '如果物体沿直线运动，为了定量描述物体的位置变化，可以以这条直线为x轴，在直线上规定原点、正方向和单位长度，建立直线坐标系。一般来说，为了定量地描述物体的位置及位置的变化，需要在参考系上建立适当的坐标系（coordinate system）。'
    tts(text=text)
