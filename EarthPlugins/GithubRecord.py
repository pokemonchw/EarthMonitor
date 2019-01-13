#!/usr/bin/python3
from urllib import request
from EarthPlugins import MessagePush,CacheHandle
import json,os,socks,socket,time
from bot_constant import GITHUB_TOKEN,PROXY_IP,PROXY_PORT,GITHUB_API_URL

headers = {
    'Authorization':GITHUB_TOKEN
}

# 读取github数据
def getGithubRecord():
    url = GITHUB_API_URL
    requestData = request.Request(url=url,headers=headers)
    try:
        http = request.urlopen(requestData)
    except Exception:
        socksDefault = socks.get_default_proxy()
        socketDefault = socket.socket
        socks.set_default_proxy(socks.SOCKS5, PROXY_IP, PROXY_PORT)
        socket.socket = socks.socksocket
        http = request.urlopen(requestData)
        socks.setdefaultproxy(socksDefault)
        socket.socket = socketDefault
    httpJson = json.loads(http.read().decode("utf-8"))
    for loop in range(0, len(httpJson), 1):
        commitsUrl = httpJson[loop]['commits_url']
        commitName = httpJson[loop]['name']
        commitsUrl = str(commitsUrl[0:-6])
        getCommits(commitsUrl, commitName)

# 读取commits数据
def getCommits(commitsUrl,commitName):
    commitUrlData = request.Request(url=commitsUrl,headers=headers)
    try:
        commitHttp = request.urlopen(commitUrlData)
        commitJson = json.loads(commitHttp.read().decode("utf-8"))
        commitJudgment(commitJson[0], commitName)
    except Exception as e:
        eJson = json.load(e)
        if e.read() == 'HTTP Error 409: Conflict':
            pass
        elif eJson['documentation_url'] == 'https://developer.github.com/v3/#rate-limiting':
            try:
                socksDefault = socks.get_default_proxy()
                socketDefault = socket.socket
                socks.set_default_proxy(socks.SOCKS5, PROXY_IP, PROXY_PORT)
                socket.socket = socks.socksocket
                try:
                    time.sleep(2)
                    commitHttp = request.urlopen(commitUrlData)
                except:
                    time.sleep(2)
                    commitHttp = request.urlopen(commitUrlData)
                socks.setdefaultproxy(socksDefault)
                socket.socket = socketDefault
                commitJson = json.loads(commitHttp.read().decode("utf-8"))
                commitJudgment(commitJson[0], commitName)
            except Exception as e:
                if str(e) == 'HTTP Error 409: Conflict':
                    pass
                else:
                    getCommits(commitsUrl,commitName)


# commit数据判断
def commitJudgment(commit,commitName):
    baseDir = os.path.dirname(__file__)
    filePath = os.path.join(baseDir, 'data','githubLastup', commitName)
    name = commit['commit']['author']['name']
    commitTime = commit['commit']['author']['date']
    message = commit['commit']['message']
    commitList = [commitName,name,commitTime,message]
    writeJudgment(filePath,commitList)

# 读写判断
def writeJudgment(filePath,commitList):
    commitName = commitList[0]
    name = commitList[1]
    commitTime = commitList[2]
    message = commitList[3]
    commit = "repo:" + commitName + ",author:" + name + ",date:" + commitTime + ",message:" + message
    if os.path.exists(filePath) and os.path.isfile(filePath):
        file = open(filePath,'r')
        line = file.readlines()
        file.close()
        line = list(line)
        judgment = "repo:" + commitName + ",author:" + name + ",date:" + commitTime
        while str(line).find(judgment) == -1:
            githubName = "仓库:" + commitName
            pushPeople = "提交人:" + name
            pushTime = "提交时间:" + commitTime
            remarks = "备注信息:" + message
            overMessage = "同步完成，请留意"
            messagePush = "心智模型001号通信ing \n 正在为您同步commits记录:" + "\n" +\
                           githubName + "\n" +\
                           pushPeople + "\n" +\
                           pushTime + "\n" +\
                           remarks + "\n" +\
                           overMessage
            CacheHandle.nowMassageId = 'github'
            MessagePush.messagePush(messagePush)
            writeGithubLastup(commit,filePath)
            break
    else:
        CacheHandle.nowMassageId = 'github'
        messagePush = "心智模型001号通信ing \n github仓库[" + commitName + "]信息同步ing \n 同步完成,请留意"
        MessagePush.messagePush(messagePush)
        writeGithubLastup(commit, filePath)

# 写入git同步记录
def writeGithubLastup(commit,filePath):
    file = open(filePath, 'w', encoding='utf-8')
    file.write(commit)
    file.close()
