from selenium.webdriver.common.by import By

class BlazeDemoRegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    name_text_field = "name"
    company_text_field = "company"
    email_text_field = "email"
    password_text_field = "password"
    confirm_password_text_field = "password-confirm"
    register_button = "//div/button[@class='btn btn-primary']"

    def enter_name(self, name):
        self.driver.find_element(By.ID, self.name_text_field).send_keys(name)
    
    def enter_company(self, company):
        self.driver.find_element(By.ID, self.company_text_field).send_keys(company)

    def enter_email(self, emailAddress):
        self.driver.find_element(By.ID, self.email_text_field).send_keys(emailAddress)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_text_field).send_keys(password)
    
    def enter_confirmed_password(self, passwordConfirmed):
        self.driver.find_element(By.ID, self.confirm_password_text_field).send_keys(passwordConfirmed)

    def click_register_button(self):
        self.driver.find_element(By.XPATH, self.register_button).click()