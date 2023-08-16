from selenium.webdriver.common.by import By


# Locators
class RegistrationPage:
    textbox_firstname_id = "input-firstname"

    first_name = (By.ID, "input-firstname")

    textbox_lastname_id = "input-lastname"
    textbox_email_id = "input-email"
    textbox_password_id = "input-password"
    radiobutton_subscribe_id = "input-newsletter-yes"
    checkbox_policy_xpath = "//input[@name='agree']"
    button_continue_xpath = "//button[normalize-space()='Continue']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def set_firstname(self, firstname):
        firstname_text = self.driver.find_element(By.ID, self.textbox_firstname_id)
        firstname_text.send_keys(firstname)

    def set_lastname(self, lastname):
        lastname_text = self.driver.find_element(By.ID, self.textbox_lastname_id)
        lastname_text.send_keys(lastname)

    def set_email(self, email):
        email_text = self.driver.find_element(By.ID, self.textbox_email_id)
        email_text.send_keys(email)

    def set_password(self, password):
        password_text = self.driver.find_element(By.ID, self.textbox_password_id)
        password_text.send_keys(password)

    def set_subscribe(self):
        subscribe = self.driver.find_element(By.ID, self.radiobutton_subscribe_id)
        subscribe.click()

    def set_privacy_policy(self):
        self.driver.find_element(By.XPATH, self.checkbox_policy_xpath).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def get_confirmation_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None
