# 元素交互，例如点击，输入之类的
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()