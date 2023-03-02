from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
# Добавление комментария

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
read_more_btn = driver.find_element(By.CSS_SELECTOR, ".product_tag-ruby a:nth-child(2)")
read_more_btn.click()
# Нажмите на вкладку "REVIEWS"
review_tab_btn = driver.find_element(By.CLASS_NAME, "reviews_tab")
review_tab_btn.click()
# Поставьте 5 звёзд
five_stars_button = driver.find_element(By.CLASS_NAME, "star-5")
five_stars_button.click()
# Заполните поле "Review" сообщением: "Nice book!"
review_field = driver.find_element(By.ID, "comment")
review_field.send_keys("Nice book!")
# Заполните поле "Name"
name_field = driver.find_element(By.ID, "author")
name_field.send_keys("Test Name")
# Заполните "Email"
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("exmaple@gmail.com")
# Нажмите на кнопку "SUBMIT"
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()
driver.quit()
