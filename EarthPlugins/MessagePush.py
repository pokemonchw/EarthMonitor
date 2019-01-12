#!/usr/bin/python3
import notify2,subprocess,os,telegram,requests
from EarthPlugins import PushMastodon,CacheHandle
from bot_constant import *
from telegram.ext import Updater

updater = Updater(TOKEN,request_kwargs={'proxy_url':PROXY_URL})
tg_bot = updater.bot
baseDir = os.path.dirname(__file__)
startLogLockFilePath = os.path.join(baseDir, 'data', 'startLogLock')

def messagePush(message):
    startState = startLogLock()
    if startState == False and CacheHandle.nowMassageId == 'start':
        os.mknod(startLogLockFilePath)
    if CacheHandle.nowMassageId == 'start' and startState:
        pass
    else:
        systemMessage(message)
        shellMessage(message)
        tgQQMessage(message)
        mastodonMessage(message)
    CacheHandle.nowMassageId = ''

def startLogLock():
    if os.path.isfile(startLogLockFilePath):
        return True
    return False

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

def tgQQMessage(message):
    try:
        tgMessage(message)
    except telegram.error.TimedOut:
        pass
    qqMessage(message)

def tgMessage(message):
    for i in TG_LIST:
        tg_bot.send_message(i,text=message)

def qqMessage(message):
    for i in QQ_LIST:
        url = API_ROOT + 'send_group_msg?group_id=' + str(i) + '&message=' + message
        requests.post(url)

