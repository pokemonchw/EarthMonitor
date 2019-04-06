import os
import datetime
import json
from EarthPlugins import MessagePush,CacheHandle
from EarthPlugins.DailyCyclePlugins import DoomsdayClock

def startDailyCycle():
    today = str(datetime.date.today())
    baseDir = os.path.dirname(__file__)
    fileName = today + '.json'
    filePath = os.path.join(baseDir,'data','dailyCycle',fileName)
    if dateJudge == True:
        dailyCycleData = _loadjson(filePath)
    else:
        dailyCycleData = {}
    nowHour = getNowHour()
    if int(nowHour) == 0:
        if not('doomsday' in dailyCycleData) or dailyCycleData['doomsday'] != 1:
            doomsdayMessage = DoomsdayClock.getDoomsdayClockText()
            message = '心智模型001号通信ing' + '\n' + '正在为您同步末日时钟刻度' + '\n' + doomsdayMessage + '\n' + '同步完成，请留意'
            CacheHandle.nowMassageId = 'doomsday'
            MessagePush.messagePush(message)
            dailyCycleData['doomsday'] = 1
    dailyCycleDataStr = json.dumps(dailyCycleData)
    dailyCycleFile = open(filePath,'w',encoding='utf-8')
    dailyCycleFile.write(dailyCycleDataStr)
    dailyCycleFile.close()

def getNowHour():
    nowTime = datetime.datetime.now()
    return nowTime.hour

def dateJudge():
    today = str(datetime.date.today())
    return judgeFile(today)

def judgeFile(date):
    baseDir = os.path.dirname(__file__)
    fileName = date + '.json'
    filePath = os.path.join(baseDir,'data','dailyCycle',fileName)
    if os.path.exists(filePath) and os.path.isfile(filePath):
       return True
    return False

def _loadjson(filePath):
    try:
        if is_utf8bom(filePath):
            ec = 'utf-8-sig'
        else:
            ec = 'utf-8'
        with open(filePath, 'r', encoding=ec) as f:
            jsondata = json.loads(f.read())
    except json.decoder.JSONDecoderError:
        jsondata = []
    except FileNotFoundError:
        jsondata = []
    return jsondata

def is_utf8bom(pathfile):
    if b'\xef\xbb\xbf' == open(pathfile, mode='rb').read(3):
        return True
    return False
