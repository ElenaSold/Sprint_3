from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.Locators import TestLocators

#переход по клику на «Личный кабинет»
def test_go_to_personal_account_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*TestLocators.Email).send_keys("Soldatenkova1989@mail.ru")
    driver.find_element(*TestLocators.Password).send_keys("123456")
    driver.find_element(*TestLocators.Button_enter_autorization_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_account)))

    driver.find_element(*TestLocators.Button_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_exit)))

    driver.find_element(*TestLocators.Button_exit).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.Text_Log_in)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()