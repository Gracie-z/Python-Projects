from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from lxml import etree

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.implicitly_wait(5)

# login
username = driver.find_element_by_name('username')
username.send_keys('TYPE IN YOUR USERNAME')
pswd = driver.find_element_by_name('password')
pswd.send_keys('TYPE IN YOUR PASSWORD')
pswd.send_keys(Keys.RETURN)

# Save Info
save_info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
save_info.send_keys(Keys.RETURN)

# Turn on Notifications
turn_off_notif = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
turn_off_notif.click()

# Search bar: #icecream
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#icecream')
press_enter = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[2]')

press_enter.click()

# scrape images
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )
except:
    driver.quit()
source = driver.page_source
with open('source.html', 'w') as f:
    f.write(source)
web_page = etree.HTML(source)
i = 1
for image in web_page.xpath('//img/@src'):
    if "https" in image:
        print(image)

        real_image = requests.get(image)
        with open(f'icecream{str(i)}.jpg', 'wb') as f:
            f.write(real_image.content)
            i += 1

quit()
