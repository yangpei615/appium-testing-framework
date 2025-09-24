from appium.webdriver.common.appiumby import AppiumBy
from commons.base_page import BasePage
from selenium.webdriver.common.by import By

# 定义评论类
class CommentPage(BasePage):
    # 评论按钮
    comment_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.ifeng.news2gp2:id/bottom_writer_comment")'
                     )
    # 输入评论内容的文本框
    comment_input_text = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.ifeng.news2gp2:id/small_video_edit")'
                     )
    # 发送评论按钮
    comment_send_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.ifeng.news2gp2:id/submit")'
                        )
    # 评论失败提示语
    comment_fail_text = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.ifeng.news2gp2:id/login_dialog_title")'
                        )
    # 评论成功提示语
    comment_succ_text = (By.XPATH,
                     "//*[contains(@text, '评论已发送')]"
                        )



# -------------方法区-------------------
    def comment_news(self,commtext):
        """定义评论方法"""
        self.find_element(*self.news_btn).click()  #切换到新闻标签页
        self.find_element(*self.first_page_tag).click()  # 切换到头条标签页
        self.find_element(*self.first_news).click()  # 切换到第一条新闻
        self.find_element(*self.comment_btn).click()  # 点击评论按钮
        self.find_element(*self.comment_input_text).send_keys(commtext)  # 输入评论内容
        self.find_element(*self.comment_send_btn).click() # 点击发送按钮

    def comment_ok_msg(self):
        """定义评论成功方法,提示“评论已发送”"""
        try:
            comment_ok_msg = self.find_element(*self.comment_succ_text, need_wait=True).text
            return comment_ok_msg
        except:
            return None  # 或者抛出异常

    def comment_fail_msg(self):
        """定义评论失败方法，提示“当前操作需要登录帐号”"""
        try:
            # 等待弹窗标题出现
            comment_fail_msg = self.find_element(*self.comment_fail_text, need_wait=True).text
            return comment_fail_msg
        except :
            print("未捕获到提示语，可能已消失或未出现")
            return None

    def go_back(self):
        """点击返回按钮，返回上一页"""
        try:
            # 点击返回上一页按钮
            self.find_element(*self.prepage_btn,need_wait=True).click()
        except Exception as e:
            print(f"返回按钮点击失败: {e}")
            raise