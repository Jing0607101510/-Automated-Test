from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnect(5, 'b4726a2d')
componentName = 'com.netease.yanxuan.module.mainpage.activity.MainPageActivity'
device.startActivity(componentName=componentName)
MonkeyRunner.sleep(0.2)
device.touch(100, 50, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.type("大衣")
device.press('KEYCODE_ENTER')
device.touch(500, 50, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
result = device.takeSnapshot()
result.writeToFile('test.png', 'png')