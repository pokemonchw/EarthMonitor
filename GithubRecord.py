import os
import urllib.request
import json
import subprocess

# 读取github数据
def getGithubRecord():
    url = 'https://api.github.com/users/pokemonchw/repos'
    http = urllib.request.urlopen(url)
    httpJson = json.load(http)
    for loop in range(0,len(httpJson),1):
        commitsUrl = httpJson[loop]['commits_url']
        commitName = httpJson[loop]['name']
        commitsUrl = str(commitsUrl[0:-6])
        getCommits(commitsUrl,commitName)
    pass

# 读取commits数据
def getCommits(commitsUrl,commitName):
    commitHttp = urllib.request.urlopen(commitsUrl)
    commitJson = json.load(commitHttp)
    commitJudgment(commitJson[0],commitName)
    pass

# commit数据判断
def commitJudgment(commit,commitName):
    baseDir = os.path.dirname(__file__)
    filePath = os.path.join(baseDir, 'data/githubLastup', commitName)
    name = commit['commit']['author']['name']
    commitTime = commit['commit']['author']['date']
    message = commit['commit']['message']
    commitList = [commitName,name,commitTime,message]
    writeJudgment(filePath,commitList)
    pass

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
        while str(line).find(commit) == -1:
            subprocess.call("qq send group 阿里夫大陆开源社区 '地球监测站Past.1''\n'" +
                               "'致先觉，这里是心智模型001号，正在为您同步commits记录:''\n'" +
                               "'仓库:''" + commitName + "''\n'"
                               "'提交人:''" + name + "''\n'" +
                               "'提交时间:''" + commitTime + "''\n'" +
                               "'备注信息:''" + message + "''\n'"
                               "'同步完成,请留意'",shell=True)
            writeGithubLastup(commit,filePath)
            break
    else:
        subprocess.call("qq send group 阿里夫大陆开源社区 '地球监测站Past.1''\n'" +
                           "'致先觉,这里是心智模型001号,github仓库<" + commitName + ">信息同步ing'" + "'\n'" +
                           "'同步完成,请留意'",shell=True)
        writeGithubLastup(commit, filePath)
    pass
# 写入git同步记录
def writeGithubLastup(commit,filePath):
    if os.path.exists(filePath) and os.path.isfile(filePath):
        file = open(filePath, 'w', encoding='utf-8')
        file.write(commit)
        file.close()
    else:
        file = open(filePath, 'w', encoding='utf-8')
        file.write(commit)
        file.close()
    pass