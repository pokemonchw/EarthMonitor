#!/usr/bin/python3
import subprocess,time,threading
from EarthPlugins import MessagePush, GithubRecord, SeismicInformation,ArchLinuxCNRSS,CacheHandle,TyphoonInformation,CacheHandle,DailyCycle

threadPool = []

def start():
    index = 0
    threadingIdList = list(informationData.keys())
    while(True):
        for i in range(0,len(threadingIdList)):
            if threadingIdList[i] in threadPool:
                pass
            else:
                threadPool.append(threadingIdList[i])
                threadName = threadingIdList[i] + str(index)
                print(threadingIdList[i])
                nowThreading = threading.Thread(target=nowRunStart,args=(threadingIdList[i],),name=threadName,daemon=True)
                nowThreading.start()
            time.sleep(1)
        index += 1

informationData = {
    "seismicInformation":[SeismicInformation.getSeismicInformation,1800],
    "satelliteDesktop":[None,600],
    "synchronizationGithub":[GithubRecord.getGithubRecord,1800],
    "archLinuxCNRSS":[ArchLinuxCNRSS.getArchLinuxCNRSS,86400],
    "typhoonInformation":[TyphoonInformation.pushTyphoonInfo,3600],
    "typhoonNews":[TyphoonInformation.pushNews,3600],
    "startInformation":[None,86400],
    "dailyCycleInformation":[DailyCycle.startDailyCycle,60]
}

def nowRunStart(threadingId):
    sleepTime = informationData[threadingId][1]
    nowInformation = informationData[threadingId][0]
    if threadingId == 'satelliteDesktop':
        subprocess.call("himawaripy", shell=True)
    elif threadingId == 'startInformation':
        message = "链接建立完成，通信开始，监测站正常工作中"
        CacheHandle.nowMassageId = 'start'
        MessagePush.messagePush(message)
    else:
        print('get ' + threadingId + ' Now')
        try:
            nowInformation()
            print('get ' + threadingId + ' Over')
        except Exception as e:
            CacheHandle.nowMassageId = 'flowError'
            errorLog = 'get ' + threadingId + ' Null:\n' + str(e)
            MessagePush.messagePush(errorLog)
    time.sleep(sleepTime)
    threadPool.remove(threadingId)

start()
