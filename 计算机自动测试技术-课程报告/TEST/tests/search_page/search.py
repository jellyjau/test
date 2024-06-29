from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 启动浏览器
driver = webdriver.Chrome()

# 打开商城首页
driver.get("http://localhost:8080/index")

try:
    # 定位搜索框
    search_box = driver.find_element(By.CLASS_NAME,"header-right.search-box")
    search_link = search_box.find_element(By.TAG_NAME,"a")

    # 点击搜索图标
    search_link.click()
    time.sleep(3)  # 等待搜索框展开

    # 定位搜索框中的输入框和搜索按钮
    search_input = driver.find_element(By.NAME,"keyword")
    search_button = driver.find_element(By.XPATH,"//form[@class='navbar-form']/button[@type='submit']")

    # 在搜索框中输入关键词并提交搜索
    search_input.send_keys("蛋糕")        # 合法的搜索词
    # search_input.send_keys("    ")         # 无效的空白搜索词
    # search_input.send_keys("啤酒")         # 无效的搜索词

    time.sleep(2)
    search_button.click()

    # 等待搜索结果页面加载完成
    time.sleep(10)


except Exception as e:
    print("测试失败:", str(e))

finally:
    # 关闭浏览器
    driver.quit()
