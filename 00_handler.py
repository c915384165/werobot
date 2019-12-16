import werobot

robot = werobot.WeRoBot(token='hello')

#@robot.text
#def echo(message):
    #return message.content

@robot.image
def img(message):
    return message.img


@robot.text
def first(message, session)
    if 'first' in session:
          session['firkkk']
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
