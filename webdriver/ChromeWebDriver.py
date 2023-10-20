from selenium import webdriver
from time import sleep
from vars import URL_BOMCONTROLE, SHORT_SLEEP



def initializeDriver():
    driver = webdriver.Chrome()
    driver.get(URL_BOMCONTROLE)
    sleep(10)
    sleep(SHORT_SLEEP)



# def findElement(xpath, )