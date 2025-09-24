# 凤凰新闻全程自动化

from appium import  webdriver
from appium.options.android import  UiAutomator2Options
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
import time



# 抓包包名
# driver = webdriver.Remote('http://127.0.0.1:4723',options=UiAutomator2Options())
# print("包名：",driver.current_package)
# print("activity名：",driver.current_activity)


# 构造连接
driver = webdriver.Remote(
    'http://127.0.0.1:4723',
     options=UiAutomator2Options().load_capabilities({
    "appPackage": "com.ifeng.news2gp2",
    "appActivity": "com.ifeng.news2.activity.IfengTabMainActivity",
    'dontStopAppOnReset': True, # 在会话重置（reset）时，是否保持应用在后台继续运行，而不是关闭它。
    'automationName': 'UiAutomator2',  # 必须设置
    "chromedriverExecutable": r"E:\python_learning\appium_learning\chromedriver.exe"
     })
)
time.sleep(10)
driver.implicitly_wait(10)
# 点击【同意】按钮
e1 = driver.find_element(AppiumBy.ID,'com.ifeng.news2gp2:id/tv_privacy_agree')
e1.click()


# -------登录失败用例------------
# 切换到未登录tab页
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 点击登录按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/txt_login_btn")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 用户名输入框
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_account")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys('11111')
# 密码输入框
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_password")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys('123')
# 点击同意协议
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/cb_login_default")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 点击登录按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_button_login")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取登录提示
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/password_hint_error")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
msg = e1.text
print(msg)
# 断言结果
assert  msg == "密码格式不正确"
# 后置操作——关闭登录
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/back")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()




# -----------------评论失败用例-----------------------
# 切换到“新闻”标签页
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_lin").instance(0)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 切换到“头条”标签页
v = 'new UiSelector().className("android.widget.RelativeLayout").instance(14)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取第一条新闻信息
v = '//android.widget.TextView[@resource-id="com.ifeng.news2gp2:id/channel_title"][1]'
e1 = driver.find_element(AppiumBy.XPATH,v)
e1.click()
# 点击评论按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_writer_comment")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 输入评论内容
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/small_video_edit")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys("祝祖国昌盛！")
# 点击发送按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/submit")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取系统提示语
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/login_dialog_title")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
msg = e1.text
print(msg)
# 断言
assert  msg == "当前操作需要登录帐号"
# 后置操作
try:
    driver.tap([(600,1200)])
    driver.tap([(600, 1200)])
except:
    pass

time.sleep(2)
# 返回上一页
v = 'com.ifeng.news2gp2:id/detail_back_iv'
e1 = driver.find_element(AppiumBy.ID,v)
e1.click()


#-------登录成功用例-------
# 切换到未登录tab页
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 点击登录按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/txt_login_btn")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 用户名输入框
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_account")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys('15899768708')
# 密码输入框
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_password")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys('Jolie4567')
# 点击同意协议
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/cb_login_default")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 点击登录按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_button_login")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取登录成功页面
v = 'new UiSelector().text("我")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
msg = e1.text
print(msg)
# 断言结果
assert  msg == "我"
print("登录成功！")


#-------------评论成功用例-----------------------
# 切换到“新闻”标签页
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_lin").instance(0)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# v = '//android.widget.TextView[@resource-id="com.ifeng.news2gp2:id/channel_title"][1]'
# e1 = driver.find_element(AppiumBy.XPATH,v)
e1.click()
# 切换到“头条”标签页
v = 'new UiSelector().className("android.widget.RelativeLayout").instance(14)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取第一条新闻信息
v = '//android.widget.TextView[@resource-id="com.ifeng.news2gp2:id/channel_title"][1]'
e1 = driver.find_element(AppiumBy.XPATH,v)
e1.click()
# 点击评论按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_writer_comment")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 输入评论内容
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/small_video_edit")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.send_keys("祝祖国昌盛！")
# 点击发送按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/submit")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取系统提示语
try:
    toast_element = WebDriverWait(driver, 5, poll_frequency=0.1).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@text, '评论已发送')]"))
    )
    print("捕获到提示语:", toast_element.text)
except:
    print("未捕获到提示语，可能已消失或未出现")
# 返回上一页
v = 'com.ifeng.news2gp2:id/detail_back_iv'
e1 = driver.find_element(AppiumBy.ID,v)
e1.click()



#-------------收藏用例-----------------------
# 获取第一条新闻信息
v = '//android.widget.TextView[@resource-id="com.ifeng.news2gp2:id/channel_title"][1]'
e1 = driver.find_element(AppiumBy.XPATH,v)
title = e1.text[:10]  # 获取标题的前10个字
print(title)
e1.click()
# 点击收藏按钮
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_collection")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 获取系统提示语
try:
    toast_element = WebDriverWait(driver, 5, poll_frequency=0.1).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@text, '收藏成功')]"))
    )
    print("捕获到提示语:", toast_element.text)
except:
    print("未捕获到提示语，可能已消失或未出现")
# 返回上一页
v = 'com.ifeng.news2gp2:id/detail_back_iv'
e1 = driver.find_element(AppiumBy.ID,v)
e1.click()
# 切换到我的页面
v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 点击收藏按钮
v = 'new UiSelector().text("收藏")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()
# 判断title内容是否在收藏列表中
v = f'//android.view.View[starts-with(@content-desc,"{title}")]'
el = driver.find_element(AppiumBy.XPATH, v) # 获取第二个元素
new_title = el.get_attribute('content-desc')[:10] # 内容不在text中
print(new_title)
assert title == new_title
# 返回上一页
v = 'new UiSelector().className("android.widget.ImageView")'
e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
e1.click()



# #-------------关注用例-----------------------
# # 切换到新闻页面
# v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(0)'
# e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# e1.click()
# #  切换到关注页面
# v = 'new UiSelector().text("关注").instance(0)'
# e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# e1.click()
# # 选择第一条未被关注的内容，点击关注按钮
# v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tv_card_wemedia_add_sub").instance(0)'
# e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# e1.click()
# # 获取关注的栏目名称
# v = 'com.ifeng.news2gp2:id/tv_card_wemedia_name'
# e1 = driver.find_element(AppiumBy.ID,v)
# column_name  = e1.text  # 保存关注的栏目名称
# print("关注的栏目名称:",column_name )
# e1.click()
# time.sleep(2)
# # 获取系统提示语
# try:
#     toast_element = WebDriverWait(driver, 5, poll_frequency=0.1).until(
#         EC.presence_of_element_located((By.XPATH, "//*[contains(@text, '关注成功')]"))
#     )
#     print("捕获到提示语:", toast_element.text)
# except:
#     print("未捕获到提示语，可能已消失或未出现")
# # 切换到我的页面
# v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
# e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# e1.click()
# # 点击关注列表
# v = 'new UiSelector().resourceId("com.ifeng.news2gp2:id/txt_follow_title")'
# e1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,v)
# e1.click()
# # 获取最新的关注内容
# v = 'com.ifeng.news2gp2:id/new_subscription_name'
# e1 = driver.find_element(AppiumBy.ID,v)
# followed_name = e1.text
# print(followed_name)
# assert  followed_name == column_name
# print("已成功关注内容")
# # 返回上一页
# v = 'com.ifeng.news2gp2:id/img_back_sub'
# e1 = driver.find_element(AppiumBy.ID,v)
# e1.click()


