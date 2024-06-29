from telnetlib import EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()

# 打开登录页面
driver.get('http://localhost:8080/user_login.jsp')

try:
    # 找到用户名输入框并输入用户名
    username_input = driver.find_element('name', 'ue')
    # 1.正确的登录信息
    username_input.send_keys('admin')
    # username_input.send_keys('roro')
    # 找到密码输入框并输入密码
    password_input = driver.find_element('name', 'password')
    # 1.输入正确的密码
    password_input.send_keys('admin')
    # password_input.send_keys('roro123')


    # 等待一段时间以便查看输入结果
    time.sleep(7)

    # 找到提交按钮并点击
    submit_button = driver.find_element('xpath', '//input[@type="submit"]')
    submit_button.click()
    print("登录成功")
except Exception as e:
    print("测试失败:", str(e))
# 等待页面加载完成
time.sleep(2)

# 获取当前页面的标题
page_title = driver.title

# 断言页面标题是否与预期相符
assert page_title == '个人中心'

try:
    # 找到后台管理并点击  <a href="/admin/index.jsp" target="_blank">后台管理</a>
    admin_link = driver.find_element(By.LINK_TEXT, "后台管理")
    admin_link.click()

    # 切换到新打开的窗口
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)
    # 获取页面当前的URL
    current_url = driver.current_url

    # 断言页面是否跳转到后台管理页面http://localhost:8080/admin/index.jsp
    assert current_url == "http://localhost:8080/admin/index.jsp", f"跳转失败，当前URL为：{current_url}"

    print("跳转到后台管理页面测试成功")

except Exception as e:
    print("测试失败:", str(e))


# 找到类目管理并点击<a href="/admin/type_list">类目管理</a>
try:
    category_link = driver.find_element(By.LINK_TEXT, "类目管理")
    category_link.click()
    # 等待跳转后的页面加载完成
    driver.switch_to.window(driver.window_handles[1])

    # 获取当前页面的URL
    current_url = driver.current_url

    # 断言页面是否跳转到类目管理页面
    assert current_url == "http://localhost:8080/admin/type_list", f"跳转失败，当前URL为：{current_url}"

    print("跳转到类目管理页面测试成功")

except Exception as e:
    print("测试失败:", str(e))

time.sleep(3)
try:
    # 定位输入框并输入类目
    input_name = driver.find_element(By.ID, "input_name")
    # input_name.send_keys("大学生必吃系列")
    # input_name.send_keys("            ")
    input_name.send_keys("小学生爱吃系列")

    time.sleep(3)
    # 定位提交按钮并点击
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()
    print("添加类目测试成功")
except Exception as e:
    print("测试失败:", str(e))


time.sleep(10)
# 关闭浏览器
driver.quit()
