#!/usr/bin/python3
import notify2

def messagePush(message):
    systemMessage(message)
    pass

def systemMessage(message):
    notify2.init("地球监测站")
    earthMonitorPush = notify2.Notification("地球监测站Past.1",message)
    earthMonitorPush.set_hint("x",10)
    earthMonitorPush.set_hint("y",10)
    earthMonitorPush.show()
    pass

