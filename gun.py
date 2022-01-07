from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


option = webdriver.ChromeOptions()
# option.add_argument('headless')  设置option
browser = webdriver.Chrome(options=option)
browser.get("http://game2.baifumeiba.com/minigame/ydygdy/")
time.sleep(3)
ele = browser.find_element(By.ID, "c2canvas")
ActionChains(browser).move_by_offset(491, 615).click_and_hold().erform()
time.sleep(2)
ActionChains(browser).drag_and_drop_by_offset(491, 0).perform()
time.sleep(5)
