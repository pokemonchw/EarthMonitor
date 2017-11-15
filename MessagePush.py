#!/usr/bin/python3
import notify2

def messagePush(message):
    systemMessage(message)
    pass

def systemMessage(message):
    notify2.init("地球监测站")
    maxList = len(message)
    earthMonitorPush = notify2.Notification("地球监测站Past.1",message)
    earthMonitorPush.set_hint("x",1)
    earthMonitorPush.set_hint("y",3)
    earthMonitorPush.show()
    pass

