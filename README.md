地球监测站
====================

EarthMonitor
====================

说明
---

这是一个基于python的bot仓库\
自用为主，不考虑面向服务扩展\
基于GPL协议开源\
持续开发ing\

外部支持
----

依赖于himawaripy项目\
地址:https://github.com/boramalper/himawaripy\
依赖于qqbot项目\
地址:https://github.com/pandolia/qqbot\

主要用途
----

该项目主要用于对地震灾害进行采集，以及本地服务实行管理

预定计划
----

telegram,irc,qq消息同步\
台风信息采集\
新闻检索--刑事犯罪信息采集\
byayoi开源社区(待建设)防护\
其他(看心情)

使用说明
----

以下是某人的无责说明\
因为丢上github只是为了方便版本控制和装哔————\
所以很不建议有人使用本监测站\
但是，或许会有人抱着交流学习的目的下载下去玩耍也说不定？\
那么就写一点说明\
目前的版本是以SeismicInformation.py为核心\
地震信息储存在data目录下，6.5级以上会通过qqbot的接口发送消息至q群\
该发送命令只在konsole下进行过测试，不建议在任何非linux系统进行尝试\
同样的，你可以发送到自己的bot中，该数据采集自:earthquake.usgs.gov\
不使用himawaripy(向日葵8号气象卫星拍摄照片同步桌面)的话，注释掉Main.py中第31行即可\
当然，建议你最好自己写一个bot\
目前的版本没什么复杂的功能，爬虫逻辑也很简单\
该爬虫参考了https://github.com/hxy513696765/Python-monitor-earthquake/ \
若要执行检测站，只需在项目目录下执行./Main.py即可\
特别警告，千万不要放入crontab中\
写在最后，对本项目有任何使用上的困难，请自行解决\

作者
---
任悠云

联系方式
-----------
mail:admin@byayoi.org