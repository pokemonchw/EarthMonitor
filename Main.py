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
    for t in [tA, tC, tB]:
        t.setDaemon(True)
        t.start()
    tB.join(6500)
    tA._stop()
    tC._stop()
    tB._stop()
    job()
    pass

def seismicInformation():
    SeismicInformation.getSeismicInformation()
    pass

def satelliteDesktop():
    subprocess.call("himawaripy", shell=True)
    time.sleep(600)
    pass

def synchronizationGithub():
    GithubRecord.getGithubRecord()
    pass

def startInformation():
    subprocess.call("qq send group 阿里夫大陆开源社区 '地球监测站Past.1''\n''链接建立完成，通信开始，监测站正常工作中'",shell=True)
    pass

start()