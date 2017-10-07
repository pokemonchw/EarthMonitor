#!/usr/bin/python3
import threading
import subprocess

import time

import GithubRecord
import SeismicInformation

def start():
    startInformation()
    job()
    pass

def job():
    tA = threading.Thread(target = seismicInformation)
    tB = threading.Thread(target = satelliteDesktop)
    tC = threading.Thread(target = synchronizationGithub)
    for t in [tA, tB, tC]:
        t.setDaemon(True)
        t.start()
    tA.join(6500)
    tB.join(6500)
    tC.join(6500)
    tA._stop()
    tB._stop()
    tC._stop()
    job()
    pass

def seismicInformation():
    SeismicInformation.getSeismicInformation()
    time.sleep(300)
    pass

def satelliteDesktop():
    subprocess.call("himawaripy", shell=True)
    pass

def synchronizationGithub():
    GithubRecord.getGithubRecord()
    time.sleep(300)
    pass

def startInformation():
    subprocess.call("qq send group 阿里夫大陆开源社区 '地球监测站Past.1''\n''链接建立完成，通信开始，监测站正常工作中'",shell=True)
    pass

start()