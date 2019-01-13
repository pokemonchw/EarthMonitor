#!/usr/bin/python3
import notify2,subprocess,os,telegram,requests,os,datetime
from EarthPlugins import PushMastodon,CacheHandle
from bot_constant import *
from telegram.ext import Updater

updater = Updater(TOKEN,request_kwargs={'proxy_url':PROXY_URL})
tg_bot = updater.bot
baseDir = os.path.dirname(__file__)
startLogLockFilePath = os.path.join(baseDir, 'data', 'startLogLock')

putClassData = {
    "start":["system","shell","qq","tg","mastodon"],
    "github":["system","shell","qq","tg","mastodon"],
    "archLinuxCNRSS":["system","shell","qq","tg","mastodon"],
    "seismic":["system","shell","qq","tg","mastodon"],
    "typhoon":["system","shell","qq","tg","mastodon"],
    "mastodonError":["system","shell","log"],
    "flowError":["system","shell","log"]
}

def messagePush(message):
    startState = startLogLock()
    if startState == False and CacheHandle.nowMassageId == 'start':
        os.mknod(startLogLockFilePath)
    if CacheHandle.nowMassageId == 'start' and startState:
        pass
    else:
        putList = putClassData[CacheHandle.nowMassageId]
        for key in putList:
            eval(putClassData[key] + 'Message')(message)
            putMessageDict[key](message)
    CacheHandle.nowMassageId = ''

def startLogLock():
    return os.path.isfile(startLogLockFilePath)

def systemMessage(message):
    notify2.init("地球监测站")
    earthMonitorPush = notify2.Notification("地球监测站Past.1",message)
    earthMonitorPush.set_hint("x",10)
    earthMonitorPush.set_hint("y",10)
    earthMonitorPush.show()

def shellMessage(message):
    subprocess.call("echo '地球监测站Past.1 \n" + message + "'", shell=True)

def mastodonMessage(message):
    PushMastodon.pushMessage(message)

def tgMessage(message):
    for i in TG_LIST:
        tg_bot.send_message(i,text=message)

def logMessage(message):
    nowTime = datetime.datetime.now()
    year = nowTime.year
    month = nowTime.month
    day = nowTime.day
    logTime = str(year) + str(month) + str(day)
    logPath = os.path.join(baseDir,'data','log',logTime)
    if os.path.isfile(logPath):
        logFile = open(logPath,'a',encoding='utf-8')
    else:
        logFile = open(logPath,'w',encoding='utf-8')
    logFile.write('\n' + str(message))
    logFile.close()



def qqMessage(message):
    for i in QQ_LIST:
        url = API_ROOT + 'send_group_msg?group_id=' + str(i) + '&message=' + message
        requests.post(url)

