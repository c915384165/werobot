import werobot
from werobot import WeRoBot
robot = WeRoBot(token='hello')
robot.config["APP_ID"] = "wxcaa52422b496346e"
robot.config["APP_SECRET"] = "a28121f72ba854b686df28ad3e28f3fc"

client = robot.client

client.create_menu({
	"button":[{
		"type": "click",
		"name": "today music",
		"key": "music"
	}],
	"button":[{
		"type": "click",
		"name": "today text",
		"key": "text"
	}]
})


@robot.key_click("music")
def music(message):
	return 'you had click on the text_button'


@robot.key_click("text")
def music(message):
	return 'you had click on the text_button'


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
