from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

#  定义一个公共父类
class BasePage:
    # 一旦对象被创建，获取实例属性驱动
    def __init__(self, driver):
        self.driver = driver

    # 定义一个类方法完成显示等待
    # 由于类方法中，不能使用实例属性，那么将类方法改成实例方式
    def wait(self, func):
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法，结合显示等待
    def find_element(self, by, value, need_wait=False):
        def f(driver):
            if driver.find_element(by, value).text:
                msg = driver.find_element(by, value).text
                # 元素需要获取文本需要就可以传递实参为True来返回文本内容
                if need_wait:
                    # #当获取元素的文本，该元素存在但是没有出现文本，那么将空文本替换直到有文本才返回
                    return msg.replace(" ","")
                else:
                    return True
            else:
                return True
            # 一旦调用重写的find_element方法，那么先触发显示等待

        self.wait(f)
        # 触发完显示等待之后，使用原生find_element定位元素操作
        return self.driver.find_element(by, value)


#-------------- 定义公共元素---------------------
    # 未登录页面
    no_login_page = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
                 )
    # 新闻tab页面
    news_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_lin").instance(0)'
    )
    # “头条”标签页
    first_page_tag = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().className("android.widget.RelativeLayout").instance(14)'
                     )
    # 第一条新闻
    first_news = (AppiumBy.XPATH,
                     '//android.widget.TextView[@resource-id="com.ifeng.news2gp2:id/channel_title"][1]'
                     )
    # 返回上一页
    prepage_btn = (AppiumBy.ID,
                'com.ifeng.news2gp2:id/detail_back_iv'
    )

