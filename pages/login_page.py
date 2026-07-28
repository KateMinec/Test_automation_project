from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    # Локаторы
    HEADER_LOGIN_BTN = (By.XPATH, "//div[@class='header-login v-popper--has-tooltip']")
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_LOGIN_BTN = (By.XPATH, "//button[contains(@class, 'gtm-login-main')]")
    LOGIN_DIALOG = (By.XPATH, "//div[@class='dialog__container']")

    # Методы
    def login(self, email, password):
        self.wait_for_clickable(self.HEADER_LOGIN_BTN).click()
        print("Открыта форма входа.")

        self.wait_for_clickable(self.USERNAME_FIELD).send_keys(email)
        self.wait_for_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_for_clickable(self.SUBMIT_LOGIN_BTN).click()
        print("Авторизация успешна.")

    def wait_for_login_modal_to_disappear(self):
        self.wait_for_invisible(self.LOGIN_DIALOG)