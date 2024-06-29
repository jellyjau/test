

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()

# 打开登录页面
driver.get('http://localhost:8080/user_login.jsp')

# 找到用户名输入框并输入用户名
username_input = driver.find_element('name', 'ue')
# 1.正确的登录信息
username_input.send_keys('roro')

# 找到密码输入框并输入密码
password_input = driver.find_element('name', 'password')
# 1.输入正确的密码
password_input.send_keys('roro123')


# 等待一段时间（例如6秒）以便查看输入结果
time.sleep(10)

# 找到提交按钮并点击
submit_button = driver.find_element('xpath', '//input[@type="submit"]')
submit_button.click()

# 等待页面加载完成
time.sleep(2)

# 获取当前页面的标题
page_title = driver.title

# 断言页面标题是否与预期相符
assert page_title == '个人中心'

# 找到新品链接并点击
link = driver.find_element(By.XPATH, '//a[@href="/goodsrecommend_list?type=3"]')
link.click()


# 找到加入购物车按钮并点击
add_to_cart_button = driver.find_element(By.XPATH, '//input[@value="加入购物车"]')
add_to_cart_button.click()
time.sleep(6)

# 找到购物车按钮并点击
cart_button = driver.find_element(By.XPATH, '//div[@class="header-right cart"]/a')
cart_button.click()

time.sleep(3)

# 找到增加按钮并点击
increase_button = driver.find_element(By.XPATH, '//a[@href="javascript:buy(10);"]')
increase_button.click()
time.sleep(3)

 # 找到减少按钮并点击
decrease_button = driver.find_element(By.XPATH, '//a[@href="javascript:lessen(10);"]')
decrease_button.click()
time.sleep(3)

# 找到删除按钮并点击
delete_button = driver.find_element(By.XPATH, '//a[@href="javascript:deletes(10);"]')
delete_button.click()
time.sleep(4)



# 关闭浏览器
driver.quit()
