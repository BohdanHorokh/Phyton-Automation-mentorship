from selenium import webdriver


def chrome_driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
