from selenium.webdriver.common.by import By

class BlazeDemoResetPasswordPage:

    def __init__(self, driver):
        self.driver = driver
    
    email_text_field = "email"
    password_reset_button = "//div/button[@class='btn btn-primary']"

    def enter_email_address(self, emailAddress):
        self.driver.find_element(By.ID, self.email_text_field).send_keys(emailAddress)

    def click_password_reset_button(self):
        self.driver.find_element(By.XPATH, self.password_reset_button).click()