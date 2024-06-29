
# 本代码是采用seleniumapi进行注册的测试的代码

from selenium import webdriver
import time

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()

# 打开注册页面
driver.get('http://localhost:8080/user_register.jsp')

# 找到用户名输入框并输入用户名
username_input = driver.find_element('name', 'username')
username_input.send_keys('dada7')

# 找到邮箱输入框并输入邮箱
email_input = driver.find_element('name', 'email')
# 输入符合要求的邮箱信息
email_input.send_keys('dada7@example.com')
# 输入不规范的邮箱信息
# email_input.send_keys('_12131')
# email_input.send_keys('12131')
# email_input.send_keys('***___')

# 找到密码输入框并输入密码
password_input = driver.find_element('name', 'password')
password_input.send_keys('dada123')

# 找到收货人输入框并输入收货人姓名
name_input = driver.find_element('name', 'name')
name_input.send_keys('dada')

# # 找到收货电话输入框并输入收货电话号码
phone_input = driver.find_element('name', 'phone')
phone_input.send_keys('1234567890')

# 找到收货地址输入框并输入收货地址
address_input = driver.find_element('name', 'address')
address_input.send_keys('海珠区东沙街24号')

# 等待一段时间以便查看输入结果
time.sleep(6)

# 找到提交按钮并点击
submit_button = driver.find_element('xpath', '//input[@type="submit"]')
submit_button.click()

# 等待页面加载完成
time.sleep(6)

# 获取当前页面的标题
page_title = driver.title

# 断言页面标题是否与预期相符
assert page_title == '用户登录'

# 关闭浏览器
driver.quit()
