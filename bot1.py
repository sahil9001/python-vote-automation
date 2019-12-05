import time 
from selenium import webdriver
#from selenium.common.keys import keys

driver = webdriver.Firefox()
driver.get('YOUR_POLL_LINK')
time.sleep(5)
driver.find_element_by_id("ELEMENT_ID").click()
time.sleep(1)
driver.find_element_by_id("CONFIRM_ID").click()
#driver.find_element_by_css_selector("").click()
#driver.FindElement(By.XPath("//div[@class='option_enclosure_2']/span[@class='option_text']"));

time.sleep(5)

driver.refresh()
driver.close()

