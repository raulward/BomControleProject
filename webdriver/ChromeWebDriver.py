from selenium import webdriver
from time import sleep
from vars import URL_BOMCONTROLE, SHORT_SLEEP



def initializeDriver():
    driver = webdriver.Chrome()
    driver.get(URL_BOMCONTROLE)
    sleep(10)
    sleep(SHORT_SLEEP)

    screenWidth = driver.execute_script("return window.screen.width;")
    screenHeight = driver.execute_script("return window.screen.heigth;")

    driver.set_window_size(screenWidth, screenHeight)


# def findElement(xpath, )