from selenium.webdriver.common.by import By

class BlazeDemoLogin:

    def __init__(self, driver):
        self.driver = driver

    email_address_text_field = "email"
    password_text_field = "password"
    login_button = "//div/button[@class='btn btn-primary']"

    def enter_email(self, emailAddress):
        self.driver.find_element(By.ID, self.email_address_text_field).send_keys(emailAddress)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_text_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()