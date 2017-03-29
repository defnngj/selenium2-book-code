from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# 指定浏览器及驱动的路径
binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\driver\\geckodriver.exe")


