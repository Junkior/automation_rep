from selenium import webdriver


def browser():
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver




