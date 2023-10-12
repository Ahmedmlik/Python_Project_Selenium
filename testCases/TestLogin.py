from pageObjects.Login import Login
from utilites.readProperties import ReadConfig
from utilites.newCustomLogger import LogGen
class Test_001_Login:
    URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen(".\\Logs\\automation.log")

    def test_homepage(self, setup):
        self.logger.log_info("*************** TestLogin *****************")
        self.logger.log_info("****Started Home page title test ****")
        self.driver = setup
        self.logger.log_info("****Opening URL****")
        self.driver.get(self.URL)
        actualTitle = self.driver.title
        if actualTitle == "Your store. Login":
            self.logger.log_info("**** Home page title test passed ****")
            assert True
            self.driver.close()

        else:
            self.logger.log_error("**** Home page title test failed****")
            self.driver.save_screenshot("..\\Screeshots\\test_homepageTitle1.png")
            self.driver.close()
            assert False


    def test_Login(self, setup):
        self.logger.log_info("****Started Login Test****")
        self.driver=setup
        self.driver.get(self.URL)
        self.Login = Login(self.driver)
        self.Login.set_user(self.username)
        self.Login.set_mp(self.password)
        self.Login.cnx_click()
        actueltitle = self.driver.title
        if actueltitle == 'Dashboard / nopCommerce administration':
            self.logger.log_info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screeshots\\test_Login.png")
            self.logger.log_error("****Login test failed ****")
            self.driver.close()
            assert False
