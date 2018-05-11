from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

user=" "  # your fb email
pwd=" "  # your facebook password




driver =webdriver.Chrome('/usr/local/bin/chromedriver')  #  your chromdriver location
driver.get("https://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem=driver.find_element_by_id("pass")

elem.send_keys(pwd)
elem=driver.find_element_by_id("loginbutton")
elem.send_keys(Keys.RETURN)
time.sleep(300)

# Facebook logout.
# logout1=driver.find_element_by_css_selector("#userNavigationLabel")
# logout1.click()
# time.sleep(2)
# logout2=driver.find_element_by_css_selector("li._54ni:nth-child(12) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
# logout2.click() 

# Closing Browser.
driver.quit()



