from selenium.webdriver.common.by import By


class MyAccountPage:
    dropdown_logout_xpath = ""

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.dropdown_logout_xpath)