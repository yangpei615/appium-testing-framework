from appium.webdriver.common.appiumby import AppiumBy
from commons.base_page import BasePage


# 定义登录类
class LoginPage(BasePage):
    # 登录按钮（未登录前的按钮）
    login_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("com.ifeng.news2gp2:id/txt_login_btn")'
                 )
    # 用户名输入框
    user_input = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_account")'
                  )
    # 密码输入框
    password_input = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_input_user_password")'
                      )
    # 同意协议的按钮
    agree_checkbox = (AppiumBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().resourceId("com.ifeng.news2gp2:id/cb_login_default")'
                      )
    # 登录按钮（输入账号密码后的登录按钮）
    login_agree_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().resourceId("com.ifeng.news2gp2:id/ul_button_login")'
                       )
    # 登录成功"我"页面
    login_ok_text = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("我")'
                     )
    # 登录失败提示
    login_fail_msg = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().resourceId("com.ifeng.news2gp2:id/password_hint_error")'
                       )
    # 关闭登录按钮
    close_login_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().resourceId("com.ifeng.news2gp2:id/back")'
                       )
    # 登录成功后设置按钮
    set_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().className("android.widget.RelativeLayout").instance(7)'
                       )
    # 退出登录按钮
    login_exit_btn = (AppiumBy.ANDROID_UIAUTOMATOR,
                       'new UiSelector().resourceId("com.ifeng.news2gp2:id/home_logout_btn")'
                       )


# -------------方法区-------------------
    def  login(self,username,password):
        """登录方法"""
        self.find_element(*self.no_login_page).click()  # 点击未登录的tab页
        self.find_element(*self.login_btn).click()  # 点击未登录的红色按钮
        self.find_element(*self.user_input).send_keys(username)  # 输入用户名
        self.find_element(*self.password_input).send_keys(password) # 输入密码
        self.find_element(*self.agree_checkbox).click()  # 勾选同意框
        self.find_element(*self.login_agree_btn).click()  # 点击登录button

    def get_login_success_text(self):
        """获取登录成功后的文本（比如“我”）"""
        try:
            login_ok_msg = self.find_element(*self.login_ok_text, need_wait=True).text
            return login_ok_msg
        except:
            return None  # 或者抛出异常

    def get_login_error_msg(self):
        """获取登录失败的错误提示"""
        try:
            login_fail_msg = self.find_element(*self.login_fail_msg, need_wait=True).text
            return login_fail_msg
        except:
            return None  # 找不到元素返回 None

    def is_logged_in(self):
        """判断是否已登录：检查‘我’元素是否存在且可见"""
        try:
            element = self.find_element(*self.login_ok_text, need_wait=True)
            return element.is_displayed()
        except:
            return False

    def login_exit(self):
        """执行登出操作，并验证是否退出成功,验证方式：退出后是否出现“登录按钮”（未登录状态下的入口）"""
        try:
            self.find_element(*self.login_ok_text).click() # 1. 进入登录成功"我"页面
            self.find_element(*self.set_btn).click()          # 2. 进入设置
            self.find_element(*self.login_exit_btn).click() # 3. 点击退出登录
            print("已点击【退出登录】按钮")
        except Exception as e:
            print(f"登出操作失败：{e}")
            return False  # 操作失败直接返回 False
        # ------- 验证退出是否成功 -------
        try:
            # 使用 BasePage 的等待机制查找登录按钮
            login_btn = self.find_element(*self.login_btn, need_wait=True)
            if login_btn.is_displayed():
                print("退出登录成功：已检测到【登录】按钮")
                return True
            else:
                print("退出登录失败：登录按钮存在但不可见")
                return False
        except Exception as e:
            print(f"退出登录失败：未找到登录按钮（异常：{e}）")
            return False







