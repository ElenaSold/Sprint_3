from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.Locators import TestLocators

#Переход из личного кабинета в конструктор нажатием на "Конструктор"
def test_go_to_assembling_from_accout_page_button_assembling():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*TestLocators.Email).send_keys("Soldatenkova1989@mail.ru")
    driver.find_element(*TestLocators.Password).send_keys("123456")
    driver.find_element(*TestLocators.Button_enter_autorization_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_account)))

    driver.find_element(*TestLocators.Button_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_assembling)))

    driver.find_element(*TestLocators.Button_assembling).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

#Переход из личного кабинета в конструктор нажатием на логотип
def test_go_to_assembling_from_accout_page_button_logo():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*TestLocators.Email).send_keys("Soldatenkova1989@mail.ru")
    driver.find_element(*TestLocators.Password).send_keys("123456")
    driver.find_element(*TestLocators.Button_enter_autorization_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_account)))

    driver.find_element(*TestLocators.Button_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
    (TestLocators.Button_logo)))

    driver.find_element(*TestLocators.Button_logo).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()