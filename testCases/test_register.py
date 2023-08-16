import os
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import RegistrationPage
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class TestRegister:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()  # for logging

    def test_account_register(self, setup):
        self.logger.info("________________ test_register started ___________________")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application.")
        self.driver.maximize_window()
        self.driver.implicitly_wait(7)

        self.homepage = HomePage(self.driver)
        self.logger.info("Clicking on My Account --> Register.")
        self.homepage.click_my_account()
        self.homepage.click_register()

        self.logger.info("Providing user details for registration.")
        self.registration_page = RegistrationPage(self.driver)
        self.registration_page.set_firstname("Ibrahim")
        self.registration_page.set_lastname("Adekunle")
        # importing function from utilities to generate random email
        self.email = randomString.random_string_generator()+'@gmail.com'
        self.registration_page.set_email(self.email)
        self.registration_page.set_password("pass1290")
        time.sleep(5)
        self.registration_page.set_subscribe()
        self.registration_page.set_privacy_policy()
        self.registration_page.click_continue_button()
        time.sleep(5)
        self.confmsg = self.registration_page.get_confirmation_msg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed.")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_account_reg.png")
            self.logger.error("Account registration is failed.")
            self.driver.close()
            assert False

        self.logger.info("*** test_register completed ***")
