#coding:utf-8
# Filename:hello_world.py
# 验证服务器，并且收到的所有消息都回复"Hello World!

import werobot

robot = werobot.WeRoBot(token="hello")

@robot.handler #  处理所有消息
def hello(message):
  return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config["APP_ID"] = "wx99e707eb6a1fa866"
# robot.config["APP_SECRET"] = "a28121f72ba854b686df28ad3e28f3fc"
robot.run()
