import pandas as pd
import time
from selenium import webdriver



path = "Users/gracezhou/PycharmProjects/chromedriver"
driver = webdriver.Chrome(driverpath = path)
url = "https://www.instagram.com/"

def site_login():
    driver.get(url)
    username = driver.find_element_by_name("username")
    pswd = driver.find_element_by_name("password")
    type_username = "hermionegrace@outlook.com"
    type_pswd = "Dfl1957n"
    username.send_keys(type_username)
    pswd.send_keys(type_pswd)
    login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]")

