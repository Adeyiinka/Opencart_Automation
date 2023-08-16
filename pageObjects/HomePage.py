from selenium.webdriver.common.by import By


class HomePage:
    nav_myaccount_xpath = "//span[normalize-space()='My Account']"
    dropdown_register_linktext = "Register"
    dropdown_login_linktext = "Login"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.nav_myaccount_xpath).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.dropdown_register_linktext).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.dropdown_login_linktext).click()
