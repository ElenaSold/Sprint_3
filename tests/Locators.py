from selenium.webdriver.common.by import By

class TestLocators:
    #поле Email
    Email = (By.XPATH, ".//input[@type='text']")
    #поле Пароль
    Password = (By.XPATH, ".//input[@type='password']")
    #кнопка "Войти" на странице авторизации
    Button_enter_autorization_page = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    #кнопка "Оформить заказ"
    Button_make_an_order = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    #сообщение "Некорректный пароль"
    Wrong_password = (By.XPATH, ".//p[@class='input__error text_type_main-default']")
    #кнопка "Войти в аккаунт"
    Button_sign_in = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    #кнопка "Личный кабинет"
    Button_account = (By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']/a")
    #кнопка "Войти" на странице регистрации
    Login_button_on_registration_page = (By.CLASS_NAME, "Auth_link__1fOlj")
    #кнопка "Войти" на странице восстановления пароля
    Login_button_on_forgot_password_page = (By.CLASS_NAME, "Auth_link__1fOlj")
    #текст "В этом разделе вы можете изменить свои персональные данные"
    Account_text = (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")
    #кнопка "Профиль"
    Button_profile = (By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
    #кнопка "История заказов"
    Button_history = (By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    #кнопка "Выход"
    Button_exit = (By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    #кнопка "Конструктор"
    Button_assembling = (By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']/ul/li/a/p")
    #кнопка логотип
    Button_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")
    #заголовок "Вход"
    Text_Log_in = (By.TAG_NAME, "h2")
    #плейсхолдер Email
    Placeholder_Email = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/label")
    #плейсхолдер Пароль
    Placeholder_Password = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/label")
    #название вкладки "Булки"
    Button_bread = (By.XPATH, ".//span[text()='Булки']")
    # название вкладки "Соусы"
    Button_sauce = (By.XPATH, ".//span[text()='Соусы']")
    # название вкладки "Начинки"
    Button_stuffing = (By.XPATH, ".//span[text()='Начинки']")
    #название текущего раздела
    Current_name = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span")




