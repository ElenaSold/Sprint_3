from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.Locators import TestLocators

#переход к разделу "Булки"
def test_assembling_bread():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*TestLocators.Button_sauce).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (TestLocators.Button_bread)))

    driver.find_element(*TestLocators.Button_bread).click()

    #проверяем, что текущий раздел - Булки
    assert driver.find_element(*TestLocators.Current_name).text == "Булки"

    driver.quit()

#переход к разделу "Соусы"
def test_assembling_sauce():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*TestLocators.Button_sauce).click()

    # проверяем, что текущий раздел - Соусы
    assert driver.find_element(*TestLocators.Current_name).text == "Соусы"

    driver.quit()

#переход к разделу "Начинки"
def test_assembling_stuffing():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*TestLocators.Button_stuffing).click()

    # проверяем, что текущий раздел - Начинки
    assert driver.find_element(*TestLocators.Current_name).text == "Начинки"

    driver.quit()


