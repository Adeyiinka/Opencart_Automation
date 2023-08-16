import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class TestLoginDDT:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir)+"\\testData\\Opencart.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("***** Starting test_myAccount *****")
        self.rows = XLUtils.get_row_count(self.path, "LoginData")
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.accountPage = MyAccountPage(self.driver)

        for r in range(2, self.rows+1):
            self.homePage.click_my_account()
            self.homePage.click_login()

            self.email = XLUtils.read_data(self.path, "LoginData", r,1)
            self.password = XLUtils.read_data(self.path, "LoginData", r, 2)
            self.exp = XLUtils.read_data(self.path, "LoginData", r, 3)
            self.loginPage.set_email(self.email)
            self.loginPage.set_password(self.password)
            self.loginPage.click_login_button()
            time.sleep(3)
            self.targetpage = self.loginPage.if_account_page_exists()

            if self.exp == "Valid":
                if self.targetpage == True:
                    lst_status.append("Pass")
                    self.accountPage.click_logout()
                else:
                    lst_status.append("Fail")
            elif self.exp == "Invalid":
                if self.targetpage == True:
                    lst_status.append("Fail")
                    self.accountPage.click_logout()
                else:
                    lst_status.append("Pass")
        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False, "Test failed"
        self.logger.info("****** End of test_myAccount ******")
