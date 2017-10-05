import urllib.request
import re
import os
import datetime
import subprocess

# 抓取网页数据
def getSeismicInformation():
    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom'
    http = urllib.request.urlopen(url)
    content = http.read().decode('utf-8')
    nation = re.findall(r'</id><title>M(.*?) - (.*?)</title><updated>',content)
    utcTime = re.findall(r'Time</dt><dd>(.*)(.*) UTC</dd><dd>', content)
    dimension = re.findall(r'</dd><dt>Location</dt><dd>(.*)&deg;(.*) (.*)&deg;(.*)</dd><dt>', content)
    informationProcessing(nation,utcTime,dimension)
    pass

# 处理数据
def informationProcessing(nation,utcTime,dimension):
    for loop in range(0, len(nation), 1):
        seismicInformation = "nagnitude:" + nation[loop][0] + \
                             ",place:" + nation[loop][1] + \
                             ",utcTime:" + utcTime[loop][0] + \
                             ",dimension:" + dimension[loop][0]
        nagnitudeJudgment(seismicInformation,nation[loop][0])
    pass

# 震级判断
def nagnitudeJudgment(seimicInformation,nagnitude):
    if float(nagnitude) >= 6.5:
        baseDir = os.path.dirname(__file__)
        filePath = os.path.join(baseDir, 'data', 'strongShock')
        alertMessage = 0
        writeJudgment(seimicInformation,filePath,alertMessage)
    else:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
        baseDir = os.path.dirname(__file__)
        filePath = os.path.join(baseDir, 'data', nowTime)
        alertMessage = 1
        writeJudgment(seimicInformation, filePath,alertMessage)
    pass

# 读写判断
def writeJudgment(seimicInformation,filePath,alerMessage):
    while alerMessage == 0:
        subprocess.call("qq send group 阿里夫大陆开源社区 '地球监测站Past.1''\n'" +
                 "'致先觉，这里是心智模型002号，正在向您传输高等地震灾害实况，具体信息为:''\n'"
                 + "'" + seimicInformation + "''\n'"  +
                 "'该信息已保存至日志中，请留意'",shell=True)
        break
    if os.path.exists(filePath) and os.path.isfile(filePath):
        file = open(filePath,'r')
        line = file.readlines()
        file.close()
        line = list(line)
        while str(line).find(seimicInformation) == -1:
            writeSeismicInformation(seimicInformation, filePath)
            break
    else:
        writeSeismicInformation(seimicInformation, filePath)
    pass

# 写入文件
def writeSeismicInformation(seimicInformation,filePath):
    if os.path.exists(filePath) and os.path.isfile(filePath):
        file = open(filePath, 'a', encoding='utf-8')
        file.write(seimicInformation + "\n")
        file.close()
    else:
        file = open(filePath, 'w', encoding='utf-8')
        file.write(seimicInformation + "\n")
        file.close()
    pass