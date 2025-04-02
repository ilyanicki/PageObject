from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.XPATH, "//a[@class='btn btn-default']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

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

class ProductPageLocators():

    #Селектор кнопки добавления в корзину
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    #Селектор названия товара
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")

    #Селектор цены товара
    PRODUCT_PRICE = (By.XPATH, "//p[@class = 'price_color']")

    #Сообщение о том что товар добавлен в корзину
    MESSAGE_ADD_TO_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")

    #Сообщение о скидке
    MESSAGE_PRICE_SALE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")

class BasketPageLocators():

    #Селектор формы товаров в корзине
    BASKET_FORM_SET = (By.XPATH,"//form[@id='basket_formset']")

    #Ceлектор сообщения о постой корзине
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")