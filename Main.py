#!/usr/bin/python3
import subprocess
import time
import threading
import GithubRecord
import SeismicInformation
import MessagePush

def start():
    startInformation()
    tA = threading.Thread(target=seismicInformation)
    tB = threading.Thread(target=satelliteDesktop)
    tC = threading.Thread(target=synchronizationGithub)
    tA.start()
    tB.start()
    tC.start()
    pass

def seismicInformation():
    SeismicInformation.getSeismicInformation()
    time.sleep(600)
    seismicInformation()
    pass

def satelliteDesktop():
    subprocess.call("himawaripy", shell=True)
    time.sleep(600)
    satelliteDesktop()
    pass

def synchronizationGithub():
    GithubRecord.getGithubRecord()
    time.sleep(600)
    synchronizationGithub()
    pass

def startInformation():
    message = "链接建立完成，通信开始，监测站正常工作中"
    MessagePush.messagePush(message)
    pass

start()