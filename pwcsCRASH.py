import csv
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup
import time

global driver
driver = webdriver.Chrome("/usr/bin/chromium/chromedriver.exe")
while True:
    driver.get("http://cabletv.pwcs.edu/cablecastapi/live?channel_id=1&use_cdn=true")
    play_click = driver.find_element_by_class_name("vjs-icon-placeholder")
    content1 = play_click.click()
    time.sleep(3)




