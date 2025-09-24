from appium.webdriver.common.appiumby import AppiumBy
from commons.base_page import BasePage
from selenium.webdriver.common.by import By


# 定义收藏类
class CollectPage(BasePage):
    # 收藏按钮
    collect_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_collection")'
                     )
    # 收藏页面系统提示语
    colle_prompt_text =  (AppiumBy.XPATH,
                '//*[contains(@text, "收藏成功")]'
    )

    # 我的页面tab页
    me_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().resourceId("com.ifeng.news2gp2:id/tab_menu_iv").instance(3)'
                   )
    # 收藏按钮
    collect_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_collection")'
                   )
    # 收藏提示语
    collect_ok_msg =  (By.XPATH,
                     "//*[contains(@text, '收藏成功')]"
                        )
    # 上一页点击按钮
    pre_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().className("android.widget.ImageView")'
                 )


# -------------方法区-------------------
    def collect_news(self):
        """定义收藏新闻的方法"""
        self.find_element(*self.news_btn).click()  # 切换到新闻标签页
        self.find_element(*self.first_page_tag).click() # 切换到头条标签页
        self.find_element(*self.first_news).click() # 切换到第一条新闻
        self.find_element(*self.collect_btn).click()  # 点击收藏按钮

    def collent_news_isok(self):
        """定义判断收藏成功的方法"""
        try:
            collect_ok_msg = self.find_element(*self.collect_ok_msg, need_wait=True).text
            return collect_ok_msg
        except:
            return None  # 或者抛出异常

    def go_pre_back(self):
        """点击返回按钮，返回上一页"""
        try:
            # 点击返回上一页按钮
            self.find_element(*self.pre_btn,need_wait=True).click()
        except Exception as e:
            print(f"返回按钮点击失败: {e}")
            raise