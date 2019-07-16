# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 06:52:26 2019

@author: khushal
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime


url_mcx_bhavcopy = "https://www.mcxindia.com/market-data/bhavcopy"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("--test-type")
chrome_options.add_argument('--incognito')
#chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox') # # Bypass OS security model
chrome_options.add_argument('disable-infobars')
'''
http://allselenium.info/file-downloads-python-selenium-webdriver/
'''

#C:\Users\khushal\Downloads\MCX_Datewise
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r"D:\MCX_Datewise",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(chrome_options=chrome_options)

actions=ActionChains(driver)

#driver.maximize_window()
driver.get(url_mcx_bhavcopy)

wait = WebDriverWait(driver, 5)

driver.execute_script("document.getElementById('cph_InnerContainerRight_C001_txtDate_hid_val').value = '20190710';")

driver.execute_script("document.getElementById('cph_InnerContainerRight_C001_txtDate_hid_val').type = 'visible';")
#//input[@id='txtDate']
#//*[@id='cph_InnerContainerRight_C001_txtDate_hid_val']
element_mcx_date = driver.find_element_by_xpath("//*[@id='cph_InnerContainerRight_C001_txtDate_hid_val']")
driver.execute_script('''
                      var element_mcx_date = arguments[0];
    var value = arguments[1];
    element_mcx_date.value = value;
                      ''', element_mcx_date, '20190709')
#element_mcx_date = driver.find_element_by_css_selector("input#cph_InnerContainerRight_C001_txtDate_hid_val")
#element_mcx_date.clear()
#element_mcx_date.send_keys("20190710")
#element_mcx_date.send_keys(Keys.RETURN)  

element_show_btn= driver.find_element_by_xpath("//*[@id='btnShowDatewise']")#.click()
actions.click(element_show_btn)
actions.perform()
time.sleep(10)


element_csv_download = driver.find_element_by_xpath("//*[@id='cph_InnerContainerRight_C001_lnkExpToCSV']")
actions.click(element_csv_download)
actions.perform()
time.sleep(15)

print("driver.current_url = ",driver.current_url)

'''
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")
'''

driver.close()
driver.quit()