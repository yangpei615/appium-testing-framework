from commons.comment_page import  CommentPage
from commons.login_page import  LoginPage



# 评论失败用例，不需要登录系统，直接点击评论
def test_comment_fail(driver):
    # 新建评论类实例
    commentpage = CommentPage(driver)
    # 执行评论方法
    commentpage.comment_news("祝祖国昌盛")
    # 获取错误提示
    error_msg = commentpage.comment_fail_msg()
    assert error_msg == "当前操作需要登录帐号", f"预期错误提示为'当前操作需要登录帐号'，实际为：{error_msg}"
    print("错误提示正确：", error_msg)
    try:
        driver.tap([(600, 1200)])

        driver.tap([(600, 1200)])
    except:
        pass
    # 点击返回上一页
    commentpage.go_back()




# 评论成功用例
def test_comment_succ(logged_in_driver):
    # 使用登录成功的fixture
    driver = logged_in_driver
    # 新建评论类实例
    commentpage = CommentPage(driver)
    # 执行评论
    commentpage.comment_news("祝祖国昌盛")
    # 获取提示
    succ_msg = commentpage.comment_ok_msg()
    assert succ_msg == "评论已发送", f"预期提示为'评论已发送'，实际为：{succ_msg}"
    print("提示正确：", succ_msg)
    # 点击返回上一页
    commentpage.go_back()

