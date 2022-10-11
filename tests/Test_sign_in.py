from selenium import webdriver
from tests.Locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#вход по кнопке «Войти в аккаунт» на главной
def test_button_sign_in():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*TestLocators.Button_sign_in).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.Text_Log_in)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(*TestLocators.Text_Log_in).text == "Вход" and driver.find_element(*TestLocators.Placeholder_Email).text == "Email" and driver.find_element(*TestLocators.Placeholder_Password).text == "Пароль"
    driver.quit()

#вход через кнопку «Личный кабинет»
def test_accaunt_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*TestLocators.Button_account).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.Text_Log_in)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(*TestLocators.Text_Log_in).text == "Вход" and driver.find_element(*TestLocators.Placeholder_Email).text == "Email" and driver.find_element(*TestLocators.Placeholder_Password).text == "Пароль"
    driver.quit()

#вход через кнопку в форме регистрации
def test_login_button_on_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*TestLocators.Login_button_on_registration_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.Text_Log_in)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(*TestLocators.Text_Log_in).text == "Вход" and driver.find_element(*TestLocators.Placeholder_Email).text == "Email" and driver.find_element(*TestLocators.Placeholder_Password).text == "Пароль"
    driver.quit()

#вход через кнопку в форме восстановления пароля
def test_login_button_on_forgot_password_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(*TestLocators.Login_button_on_forgot_password_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.Text_Log_in)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and driver.find_element(*TestLocators.Text_Log_in).text == "Вход" and driver.find_element(*TestLocators.Placeholder_Email).text == "Email" and driver.find_element(*TestLocators.Placeholder_Password).text == "Пароль"
    driver.quit()