import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input_locator = (By.NAME, 'ue')
        self.password_input_locator = (By.NAME, 'password')
        self.submit_button_locator = (By.XPATH, '//input[@type="submit"]')

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.username_input_locator)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input_locator)
        password_input.send_keys(password)

    def submit(self):
        submit_button = self.driver.find_element(*self.submit_button_locator)
        submit_button.click()

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/user_login.jsp')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        # 1.正确的登录信息
        # username_input.send_keys('admin')
        # password_input.send_keys('admin')

        self.login_page.enter_username('roro')
        self.login_page.enter_password('roro123')


        # 2.错误的登录信息
        # username_input.send_keys('testuser')
        # password_input.send_keys('testpassword')


        # 3.非法的登录信息
        # username_input.send_keys('    ')
        # password_input.send_keys('      ')



        self.login_page.submit()
        time.sleep(2)  # 等待页面加载完成
        self.assertEqual(self.driver.title, '个人中心')

    # 可以添加更多测试方法来测试不同的登录场景

if __name__ == "__main__":
    unittest.main()
