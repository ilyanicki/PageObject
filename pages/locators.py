from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    # Селекторы формы регистрации
    SIGN_UP_FORM = (By.XPATH, "//form[@id='register_form']")

    SIGN_UP_EMAIL_FIELD = (By.XPATH, "//input[@id='id_registration-email']") # Поле "Адрес электронной почты" в форме "Зарегестрироваться"
    SIGN_UP_PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password1']") # Поле "Пароль" в форме "Зарегестрироваться"
    SIGN_UP_REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password2']") # Поле "Повторите пароль" в форме "Зарегестрироваться"

    SIGN_UP_BUTTON = (By.XPATH,"//button[@name='registration_submit']") # Кнопка "Зарегестрироваться" в форме "Зарегестрироваться"

    # Селекторы формы входа
    SIGN_IN_FORM = (By.XPATH, "//form[@id='login_form']") # Форма войти

    SIGN_IN_EMAIL_FIELD = (By.XPATH, "//input[@id='id_login-username']") # Поле "Адрес электронной почты" в форме "Войти"
    SIGN_IN_PASSWORD = (By.XPATH, "//input[@id='id_login-password']") # Поле "Пароль" в форме "Войти"

    SIGN_IN_BUTTON = (By.XPATH, "//button[@name='login_submit']") # Кнопка "Войти" в форме "Войти"