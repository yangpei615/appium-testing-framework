from appium import  webdriver
from appium.options.android import  UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import pytest
from commons.login_page import LoginPage
from commons.config import conf  # 导入配置

# 抓包包名
# driver = webdriver.Remote('http://127.0.0.1:4723',options=UiAutomator2Options())
# print("包名：",driver.current_package)
# print("activity名：",driver.current_activity)


# 构造连接函数
@pytest.fixture(scope='session')
def driver():
    # 从配置项获取app信息
    d = webdriver.Remote(
        'http://127.0.0.1:4723',
        options=UiAutomator2Options().load_capabilities({
            "appPackage": conf.get_app('appPackage'),
            "appActivity": conf.get_app('appActivity'),
            'dontStopAppOnReset': True,  # 在会话重置（reset）时，是否保持应用在后台继续运行，而不是关闭它。
            'automationName': conf.get_app('automationName'),  # 必须设置
            "chromedriverExecutable": conf.get_app('chromedriverExecutable')
        })
    )
    time.sleep(10)
    d.implicitly_wait(10)
    # 点击【同意】按钮
    e1 = d.find_element(AppiumBy.ID, 'com.ifeng.news2gp2:id/tv_privacy_agree')
    e1.click()

    yield d
    d.quit()


# 定义已登录的夹具
@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """提供一个已登录的driver实例每个用例独立登录，避免状态污染"""
    page = LoginPage(driver)  # 实例化登录对象类

    #------ 前置-登录----------------
    # 1. 判断是否已登录
    if page.is_logged_in():
        print("当前已处于登录状态，跳过登录流程")
    else:
        print("当前未登录，执行登录流程...")
        #  使用配置文件中的账号密码
        username = conf.get_login("username")
        password = conf.get_login("password")
        page.login(username,password)
        # 2. 验证登录是否成功
        if not page.is_logged_in():
            raise Exception("登录失败！用户名或密码错误，或网络问题")
        print("登录成功")

    # 返回已登录的 driver
    yield driver

    # ------ 后置-登出，测试结束后退出登录---
    # 避免状态污染，保证每个用例独立
    if page.is_logged_in():  # 再次检查是否仍登录
        print("测试结束，执行登出...")
        page.login_exit()

