from selenium import webdriver
import time
import sys
from lib2to3.pgen2 import driver
from screeninfo import get_monitors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("detach", True) #try running this, this line should keep the tabs open , this didnt work in my laptop
links=['https://public.datapine.com/#board/DnjvEBVsJRVZteO3gGbSWA','https://tradytics.com/overall-market','https://www.marketwatch.com/investing/stock/live','https://www.timeanddate.com/worldclock/','https://public.datapine.com/#board/B1lHx2lJAH4qoId9jnaiMO']

x =0
y=0
flag =1
for i in range(5):
    driver=webdriver.Chrome("./chromedriver.exe",options=chrome_options)
    
    if(i*500 > 1100 and flag == 1):
        x = 0
        y += 500
        flag =0
    
    driver.set_window_position(x*500,y)
    driver.set_window_size(200,500)
    x += 1
    driver.get(links[i])
    
while(True):
    time.sleep(1)
    
    
