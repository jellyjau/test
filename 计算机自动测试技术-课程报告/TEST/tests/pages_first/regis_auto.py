

# 本代码是采用自动化测试框架,对注册信息先在配置环境中写好,然后再运行测试
import unittest
import configparser
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.driver = webdriver.Chrome()
        self.driver.get(self.config.get('TestEnvironment', 'register_url'))

    def test_user_registration(self):
        # 找到用户名输入框并输入用户名
        username_input = self.driver.find_element(By.NAME ,'username')
        username_input.send_keys(self.config.get('UserData', 'username'))

        # 找到邮箱输入框并输入邮箱
        email_input = self.driver.find_element(By.NAME ,'email')
        email_input.send_keys(self.config.get('UserData', 'email'))

        # 找到密码输入框并输入密码
        password_input = self.driver.find_element(By.NAME ,'password')
        password_input.send_keys(self.config.get('UserData', 'password'))

        # 找到收货人输入框并输入收货人姓名
        name_input = self.driver.find_element(By.NAME ,'name')
        name_input.send_keys(self.config.get('UserData', 'name'))

        # 找到收货电话输入框并输入收货电话号码
        phone_input = self.driver.find_element(By.NAME ,'phone')
        phone_input.send_keys(self.config.get('UserData', 'phone'))

        # 找到收货地址输入框并输入收货地址
        address_input = self.driver.find_element(By.NAME ,'address')
        address_input.send_keys(self.config.get('UserData', 'address'))

        # 等待一段时间以便查看输入结果
        time.sleep(3)

        # 找到提交按钮并点击
        submit_button = self.driver.find_element(By.XPATH ,'//input[@type="submit"]')
        submit_button.click()

        # 等待页面加载完成
        time.sleep(3)

        # 获取当前页面的标题
        page_title = self.driver.title



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    unittest.main()
