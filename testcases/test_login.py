from commons.login_page import  LoginPage


# 登录失败用例
def test_login_fail(driver):
    login_page = LoginPage(driver)
    # 执行登录（错误密码）
    login_page.login("11111", "123")
    # 获取错误提示
    error_msg = login_page.get_login_error_msg()
    assert error_msg == "密码格式不正确", f"预期错误提示为'密码格式不正确'，实际为：{error_msg}"
    print("错误提示正确：", error_msg)
    # 关闭登录页（可选）
    driver.find_element(*login_page.close_login_btn).click()


# 登录成功用例
def test_login_ok(driver):
    # 实例化登录对象类
    page = LoginPage(driver)
    # 执行登录函数
    page.login('15899768708','Jolie4567')
    # 获取断言
    success_text = page.get_login_success_text()
    assert  success_text == "我",f"登录成功预期显示'我'，实际为：{success_text}"
    print("登录成功！")


