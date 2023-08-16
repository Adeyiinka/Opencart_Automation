from selenium.webdriver.common.by import By


class LoginPage:
    # Locators - type of element | | locator
    textbox_email_xpath = "//input[@id='input-email']"
    textbox_password_xpath = "//input[@id='input-password']"
    button_login_xpath = "//button[normalize-space()='Login']"
    msg_my_account_xpath = "//h2[text()='My Account']"

    # Constructor - to initiate the driver
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def set_email(self, email):
        email_text = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        email_text.clear()
        email_text.send_keys(email)

    def set_password(self, password):
        password_text = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        password_text.clear()
        password_text.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def if_account_page_exists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_my_account_xpath).is_displayed()
        except:
            return False
