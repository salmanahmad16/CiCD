from selenium.webdriver.common.by import By

from pages.base_page import BaseMethods


class LoginPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.base = BaseMethods(self.driver)
        self.username_input = (By.CSS_SELECTOR, '[name="username"]')
        self.password_input = (By.CSS_SELECTOR, '[type="password"]')
        self.login_button = (By.CSS_SELECTOR, '[type="submit"]')
        self.error_message_alert = (By.CSS_SELECTOR, 'div.oxd-alert-content--error>p')

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.base.send_values(self.username_input, username)
        self.base.send_values(self.password_input, password)
        self.base.do_click(self.login_button)

    def error_message(self):
        return self.base.get_text(self.error_message_alert)




