from pages.registrationPage_BlazeDemo import BlazeDemoRegistrationPage
from utilities import excelfileReader
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestBlazeDemoRegistrationPage:

    @pytest.mark.parametrize("name, company, emailAddress, password, passwordConfirmed",
                             excelfileReader.get_data_from_excel("C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis/virtual_env/ExcelFiles/BlazeDemoExcelFile_registration_data.xlsx", "Login"))
    def test_registration_form(self, name, company, emailAddress, password, passwordConfirmed):
        type_name_in_text_field = BlazeDemoRegistrationPage(self.driver)
        type_name_in_text_field.enter_name(name)

        type_company_in_text_field = BlazeDemoRegistrationPage(self.driver)
        type_company_in_text_field.enter_company(company)

        type_email_address_in_text_field = BlazeDemoRegistrationPage(self.driver)
        type_email_address_in_text_field.enter_email(emailAddress)

        type_password_in_text_field = BlazeDemoRegistrationPage(self.driver)
        type_password_in_text_field.enter_password(password)

        type_confirmed_password_in_text_field = BlazeDemoRegistrationPage(self.driver)
        type_confirmed_password_in_text_field.enter_confirmed_password(passwordConfirmed)

        click_register = BlazeDemoRegistrationPage(self.driver)
        click_register.click_register_button()