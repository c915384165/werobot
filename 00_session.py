import werobot

robot = werobot.WeRoBot(token='hello')

@robot.text
def firsti(message, session):
	if 'first' in session:
		return 'you sent me message to me!'
	session['first'] = True
	return 'you havnt\' sent message to me'
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
