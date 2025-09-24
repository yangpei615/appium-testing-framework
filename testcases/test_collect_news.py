from commons.collent_page import  CollectPage
from commons.login_page import  LoginPage



# 收藏成功用例
def test_collect_succ(logged_in_driver):
    # 使用登录成功的fixture
    driver = logged_in_driver
    # 新建收藏类实例
    collectpage = CollectPage(driver)
    # 收藏新闻
    collectpage.collect_news()
    # 获取提示
    collect_succ_msg = collectpage.collent_news_isok()
    assert collect_succ_msg == "收藏成功", f"预期提示为'收藏成功'，实际为：{collect_succ_msg}"
    print("提示正确：", collect_succ_msg)
    # 点击返回上一页
    collectpage.go_pre_back()