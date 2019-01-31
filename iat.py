import requests
import time
import hashlib
import base64
import json

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = ""
API_KEY = ""


def getHeader(aue, engineType):
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    return header


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}

    return data


def iat():
    aue = "raw"
    engineType = "sms16k"
    audioFilePath = r"test.wav"

    r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(audioFilePath))
    info = json.loads(r.content, encoding='utf-8')
    print(info['data'])
    return info['data']


if __name__ == '__main__':
    iat()