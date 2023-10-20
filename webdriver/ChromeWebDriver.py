from selenium import webdriver
from vars import URL_BOMCONTROLE, SHORT_SLEEP, LONG_SLEEP



def initializeDriver():
    driver = webdriver.Chrome()
    driver.get(URL_BOMCONTROLE)
    



# def findElement(xpath, )