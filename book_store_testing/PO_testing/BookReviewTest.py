from selenium import webdriver
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RubyBookPO import RubyBookPage

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

start_page = StartPage(driver)

# Открыть http://practice.automationtesting.in/
start_page.goToStartPage()
# Проскроллить страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Нажать на название книги "Selenium Ruby" или на кнопку "READ MORE"
start_page.clickReadMoreButton()
ruby_book_page = RubyBookPage(driver)
# Нажать на вкладку "REVIEWS"
ruby_book_page.clickReviewsButton()
# Поставить 5 звёзд
ruby_book_page.setFiveStars()
# Заполнить поле "Review" сообщением: "Nice book!"
ruby_book_page.setReview("Nice book!")
# Заполнить поле "Name"
ruby_book_page.setName("Mike")
# Заполнить "Email"
ruby_book_page.setEmail("example@gmail.com")
# Нажать на кнопку "SUBMIT"
ruby_book_page.clickSubmitButton()

driver.quit()


