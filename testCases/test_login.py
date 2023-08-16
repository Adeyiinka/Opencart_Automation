from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class TestLogin:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()

    def test_login(self, setup):
        self.logger.info("********** Starting test_login ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.homepage = HomePage(self.driver)
        self.homepage.click_my_account()
        self.homepage.click_login()

        self.login_page = LoginPage(self.driver)
        self.login_page.set_email(self.email)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()

        self.target_page = self.login_page.if_account_page_exists()
        if not self.target_page:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//" + "test_login.png")
            assert False
        self.driver.close()
        self.logger.info("******* End of Test_login *******")

