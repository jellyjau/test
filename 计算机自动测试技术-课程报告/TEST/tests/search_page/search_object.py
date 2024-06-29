from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_locator = (By.CLASS_NAME, "header-right.search-box")
        self.search_input_locator = (By.NAME, "keyword")
        self.search_button_locator = (By.XPATH, "//form[@class='navbar-form']/button[@type='submit']")

    def open(self):
        self.driver.get("http://localhost:8080/index")

    def search(self, keyword):
        search_box = self.driver.find_element(*self.search_box_locator)
        search_link = search_box.find_element(By.TAG_NAME, "a")
        search_link.click()
        time.sleep(3)  # 等待搜索框展开
        search_input = self.driver.find_element(*self.search_input_locator)
        search_button = self.driver.find_element(*self.search_button_locator)
        search_input.send_keys(keyword)
        time.sleep(2)
        search_button.click()
        time.sleep(10)  # 等待搜索结果页面加载


# 使用Page Object模式的测试代码
driver = webdriver.Chrome()
try:
    home_page = HomePage(driver)
    home_page.open()
    home_page.search("蛋糕") # 有效的搜索词
    home_page.search("    ") # 无效的空白搜索词
    home_page.search("啤酒")  # 无效的搜索词


except Exception as e:
    print("测试失败:", str(e))
finally:
    driver.quit()
