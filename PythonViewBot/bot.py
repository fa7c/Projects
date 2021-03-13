

import time;
from selenium import webdriver;

Timer = 5

link = 'https://www.youtube.com/watch?v=hW_WFUs3hfQ&t=2s'

views = 99999

driver = webdriver.Chrome('webdrivers\chromedriver.exe')
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
  
