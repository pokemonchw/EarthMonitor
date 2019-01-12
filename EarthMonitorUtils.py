#!/usr/bin/python3
import subprocess
import time
import threading
import urllib
from EarthPlugins import MessagePush, GithubRecord, SeismicInformation,ArchLinuxCNRSS,CacheHandle,TyphoonInformation

threadPool = []

def start():
    threadList = [seismicInformation,satelliteDesktop,synchronizationGithub,archLinuxCnRss,typhoonInformation,typhoonNews,startInformation]
    threadIdList = ['seimicInformation','satelliteDesktop','synchronizationGithub','archLinuxCnRss','typhoonInformation','typhoonNews','startInformation']
    sleepTimeList = [1800,600,1800,86400,3600,3600,86400]
    index = 0
    while(True):
        for i in range(0,len(threadList)):
            if threadIdList[i] in threadPool:
                pass
            else:
                threadPool.append(threadIdList[i])
                threadName = threadIdList[i] + str(index)
                nowThreading = threading.Thread(target=threadList[i],args=(sleepTimeList[i],),name=threadName,daemon=True)
                nowThreading.start()
            time.sleep(1)

def archLinuxCnRss(sleepTime):
    print('get ArchLinuxCN RSS Now')
    try:
        ArchLinuxCNRSS.getArchLinuxCNRSS()
        print('get ArchLinuxCN RSS Over')
        time.sleep(sleepTime)
    except Exception as e:
        print('get ArchLinuxCN RSS Null:\n' + str(e))
    threadPool.remove('archLinuxCnRss')

def typhoonNews(sleepTime):
    print('get typhoonNew Now')
    try:
        TyphoonInformation.pushNews()
        print('get typhoonNew Over')
        time.sleep(sleepTime)
    except Exception as e:
        print('get typhoonNews Null:\n' + str(e))
    threadPool.remove('typhoonNews')

def seismicInformation(sleepTime):
    print('get seismic Now')
    try:
        SeismicInformation.getSeismicInformation()
        print('get seismic Over')
        time.sleep(sleepTime)
    except Exception as e:
        print('get seismic Null:\n' + str(e))
    threadPool.remove('seismicInformation')

def satelliteDesktop(sleepTime):
    subprocess.call("himawaripy", shell=True)
    time.sleep(sleepTime)
    threadPool.remove('satelliteDesktop')

def synchronizationGithub(sleepTime):
    print('get Github Now')
    try:
        GithubRecord.getGithubRecord()
        print('get Github Over')
        time.sleep(sleepTime)
    except Exception as e:
        print('get github Null:\n' + str(e))
    threadPool.remove('synchronizationGithub')

def typhoonInformation(sleepTime):
    print('get typhoonData Now')
    try:
        TyphoonInformation.pushTyphoonInfo()
        print('get typhoonData Over')
        time.sleep(sleepTime)
    except Exception as e:
        print('get typhoonData Null:\n' + str(e))
    threadPool.remove('typhoonInformation')

def startInformation(sleepTime):
    message = "链接建立完成，通信开始，监测站正常工作中"
    CacheHandle.nowMassageId = 'start'
    MessagePush.messagePush(message)

start()
