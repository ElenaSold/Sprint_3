from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.Locators import TestLocators

#успешная авторизация
def test_successful_autorization():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*TestLocators.Email).send_keys("Soldatenkova1989@mail.ru")
    driver.find_element(*TestLocators.Password).send_keys("123456")
    driver.find_element(*TestLocators.Button_enter_autorization_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.Button_make_an_order))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

#неуспешная авторизация
def test_failed_autorization():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*TestLocators.Email).send_keys("Soldatenkova1989@mail.ru")
    driver.find_element(*TestLocators.Password).send_keys("1")
    driver.find_element(*TestLocators.Button_enter_autorization_page).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(*TestLocators.Wrong_password).text == "Некорректный пароль"

    driver.quit()

