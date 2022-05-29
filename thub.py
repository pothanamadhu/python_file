import os
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.environ['PATH'] += 'C:/Users/mural/Desktop/.vs/.vscode/python/selenium/chromedriver.exe'
driver = webdriver.Chrome()
pask = ''
driver.get('https://myprofile.technicalhub.io/login')
driver.implicitly_wait(20)
driver.maximize_window()
uname = driver.find_element(By.ID, '19p31a04n8')
pas = driver.find_element(By.ID,'madhu3693')

uname.send_keys('')
pas.send_keys(pask)
login = driver.find_element(By.ID,'btn_login')
login.click()
op = driver.find_element(By.CSS_SELECTOR,'ul#nav-tabs-wrapper li:last-child')
op.click()
driver.implicitly_wait(20)

tech  = 'https://ajivika.technicalhub.io/course/view.php?id=227'
driver.get(tech)
driver.implicitly_wait(5)

links = []
elem = driver.find_elements(By.XPATH,"//*[@href]")
for i in elem:
    temp = i.get_attribute('href')
    if 'quiz' in temp:
        links.append(temp)
links = links[:]
for i in links:
    try:
        driver.get(i)
        driver.implicitly_wait(10)
        try:
            driver.find_element(By.XPATH,'//button[normalize-space()="Attempt quiz now"]').click()
            tb = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
            tb.click()
            try:
                k = 0
                while True:
                    ans = driver.find_element(By.CLASS_NAME,'r0')
                    ans.click()
                    try:
                        np = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Next page']")
                        np.click()
                        k += 1
                    except:
                        fin = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Finish attempt ...']")
                        fin.click()

                        submit = driver.find_element(By.XPATH,'//button[normalize-space()="Submit all and finish"]')
                        submit.click()

                        com = driver.find_element(By.CSS_SELECTOR,"input[type='button'][value='Submit all and finish']")
                        com.click()
                        break
        except:
            try:
                tb = driver.find_element(By.XPATH,'//button[normalize-space()="Continue the last attempt"]') 
                tb.click()
                try:
                    k = 0
                    while True:

                        ans = driver.find_element(By.CLASS_NAME,'r0')
                        ans.click()
                        try:
                            np = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Next page']")
                            np.click()
                        except:
                            fin = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Finish attempt ...']")
                            fin.click()

                            submit = driver.find_element(By.XPATH,'//button[normalize-space()="Submit all and finish"]')
                            submit.click()
            
                            com = driver.find_element(By.CSS_SELECTOR,"input[type='button'][value='Submit all and finish']")
                            com.click()
                            break
                except:
                    break
    except:
        break
