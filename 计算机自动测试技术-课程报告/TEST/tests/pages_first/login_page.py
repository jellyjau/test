
from selenium import webdriver
import time

# 设置 Chrome 驱动路径
# chrome_driver_path = '/path/to/chromedriver'

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()

# 打开登录页面
driver.get('http://localhost:8080/user_login.jsp')

# 找到用户名输入框并输入用户名
username_input = driver.find_element('name', 'ue')
# 1.正确的登录信息
# username_input.send_keys('admin')
username_input.send_keys('roro')

# 2.错误的登录信息
# username_input.send_keys('testuser')


# 3.非法的登录信息
# username_input.send_keys('    ')

# 找到密码输入框并输入密码
password_input = driver.find_element('name', 'password')
# 1.输入正确的密码
# password_input.send_keys('admin')
password_input.send_keys('roro123')

# 2.输入错误的密码信息
# password_input.send_keys('testpassword')
# 2.输入非法的密码信息
# password_input.send_keys('      ')




# 等待一段时间（例如6秒）以便查看输入结果
time.sleep(6)

# 找到提交按钮并点击
submit_button = driver.find_element('xpath', '//input[@type="submit"]')
submit_button.click()

# 等待页面加载完成
time.sleep(2)

# 获取当前页面的标题
page_title = driver.title

# 断言页面标题是否与预期相符
assert page_title == '个人中心'

# 关闭浏览器
driver.quit()
