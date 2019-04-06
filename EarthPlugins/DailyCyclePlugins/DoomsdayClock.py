#!/usr/bin/python3

from urllib import request,error
import re,time


def getDoomsdayClockText():
    url = 'https://thebulletin.org/doomsday-clock/past-announcements/'
    http = urlOpen(url)
    content = http.read().decode('utf-8')
    req = re.findall(r'uabb-infobox-title">IT IS(.*)TO MIDNIGHT',content)
    reqText = req[0]
    if ' STILL' in reqText:
        reqText = reqText.rstrip(' STILL')
    result = doomsdayInfoFanYi(reqText)
    return result

def urlOpen(url):
    try:
        req = request.Request(url)
        req.add_header('Origin',url)
        req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Mobile Safari/537.36')
        http = request.urlopen(req)
    except error.URLError:
        time.sleep(1)
        http = urlOpen(url)
    return http

def doomsdayInfoFanYi(text):
    nowMinutes = 0
    nowSecond = 0
    if 'MINUTES ' in text:
        scale = re.findall(r' (.*) MINUTES ',text)
        nowMinutes = int(scale[0])
    elif 'AND A HALF MINUTES ' in text:
        scale = re.findall(r' (.*) AND A HALF MINUTES ',text)
        nowMinutes = int(scale[0]) + 1
        nowSecond = 30
    nowTime = 60 - nowMinutes
    result = '当前末日时钟刻度为:11时' + str(nowTime) + '分' + str(nowSecond) + '秒\n距离世界末日还有:' + str(nowMinutes) + '分' + str(nowSecond) + '秒'
    if nowMinutes == 0 and nowSecond == 0:
        result = result + '\n末日来临了'
    return result
