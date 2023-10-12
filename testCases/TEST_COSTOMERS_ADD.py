import time
from pageObjects.Customers import Castomers
from pageObjects.Login import Login
from utilites.newCustomLogger import LogGen
from utilites.readProperties import ReadConfig
class Test_Costemors:
    URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    email = ReadConfig.getemail()
    name = ReadConfig.getname()
    logger = LogGen(".\\Logs\\automation.log")
    def test_addcustomer(self,setup):
        self.logger.log_info("*************** Test add customer *****************")
        self.logger.log_info("**** Started add customer verification test by validation message  ****")
        self.driver = setup
        self.logger.log_info("****Opening URL****")
        self.driver.get(self.URL)
        self.Login = Login(self.driver)
        self.Login.set_user(self.username)
        self.Login.set_mp(self.password)
        self.Login.cnx_click()
        self.costemors = Castomers(self.driver)
        self.costemors.customer()
        self.costemors.add_click()
        self.costemors.customerInfo()
        self.costemors.set_email(self.email)
        self.costemors.set_name(self.name)
        self.costemors.Save_customer()
        message_ajouter = self.costemors.verif_ajouter()
        if message_ajouter.is_displayed():
            self.logger.log_info("**** add customer verification by validation message test passed ****")
            print('message ajouter est displayed')
            self.driver.close()
            assert True
        else:
            print('message ajouter est n pas displayed')
            self.logger.log_error("**** add customer verification by validation message test failed ****")
            self.driver.close()
            assert False

    def test_add_castom_table(self,setup):
        self.logger.log_info("*************** Test add customer *****************")
        self.logger.log_info("**** Started add customer verification test by table  ****")
        self.driver = setup
        self.logger.log_info("****Opening URL****")
        self.driver.get(self.URL)
        self.costemors = Castomers(self.driver)
        self.Login = Login(self.driver)
        self.Login.set_user(self.username)
        self.Login.set_mp(self.password)
        self.Login.cnx_click()
        self.costemors.customer()
        self.costemors.add_click()
        self.costemors.customerInfo()
        self.costemors.set_email(self.email)
        self.costemors.set_name(self.name)
        self.costemors.Save_customer()
        time.sleep(2)
        n=self.costemors.nombre_rows_table()
        count=self.costemors.verifi_email_add(n,self.email)
        if count != 0 :
            print('ajouter avec succ')
            self.logger.log_info("**** add customer verification test by table test passed ****")
            self.driver.save_screenshot("..\\Screeshots\\test_add_castom_table.png")
            self.driver.close()
            assert True
        else:
            print('ajouter n pas succ')
            self.logger.log_error("**** add customer verification test by table test failed ****")
            self.driver.close()
            assert False





