from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1920,1080") # Set window size
driver = webdriver.Chrome(options=chrome_options) # Create browser driver
driver.get('https://www.google.com/search?q=python') # Search for python in google
sleep(1) # Waiting for page to load
elements = driver.find_elements_by_xpath("//div[@id='rso']/div[@class!='ULSxyf']//a[@data-ved]/h3/..") # Getting google results links
elements[4].click() # My matriculate number is 4
sleep(1) # Waiting for page to load
print('WEBSITE TITLE:')
print(driver.title) # Print website title
print('WEBSITE DESCRIPTION:')
description = driver.find_element_by_xpath("//meta[@name='description']")
print (description.get_attribute("content") ) # Print website description
driver.get_screenshot_as_file("screenshot.png") # Take an screenshot
driver.quit() # Close browser
