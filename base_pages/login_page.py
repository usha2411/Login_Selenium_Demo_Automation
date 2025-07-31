#page object
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_input=By.ID,"userName"
        self.password_input=By.ID,"password"
        self.login_button=By.ID,"login"

    def open(self):
        self.driver.get("https://demoqa.com/login")

    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_current_url(self):
        return self.driver.current_url