from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import os


os.system("clear")

banner = '''
\033[1;35moooooooooo.                          o8o  
\033[1;35m`888'   `Y8b                         `"'  
\033[1;35m 888      888  .ooooo.  oooo    ooo oooo  
\033[1;35m 888      888 d88' `88b  `88.  .8'  `888  
\033[1;35m 888      888 888ooo888   `88..8'    888  
\033[1;35m 888     d88' 888    .o    `888'     888  
\033[1;35mo888bood8P'   `Y8bod8P'     `8'     o888o 
                                          
\033[1;34m______________________________________________

\033[1;32mCreator by ; Devi
\033[1;32mFacebook id ; Devi Onfire 
\033[1;32mTool Work ; Atou Report

\033[1;34m______________________________________________
                                          
'''

print(banner)
# Prompt the user for email and password
email = input("Enter your email or phone number: ")
password = input("Enter your password: ")

# Prompt the user for the account URL and number of reports
account_url = input("Enter the account URL you want to report: ")
report_count = int(input("Enter the number of reports you want to send: "))

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")

time.sleep(4)
driver.find_element_by_id("email").send_keys(email)
time.sleep(2)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()
time.sleep(4)
driver.get(account_url)

time.sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()  # three dots
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]').click()  # find or report
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # report option
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # me
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div/div').click()  # submit
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div').click()  # next button
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()  # done
time.sleep(30)

for i in range(report_count - 1):
    driver.get(account_url)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()  # three dots
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]').click()  # find or report
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # report option
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # me
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div/div').click()  # submit
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div').click()  # next button
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()  # done
    time.sleep(30)


driver.quit()



