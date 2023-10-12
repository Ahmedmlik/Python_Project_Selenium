import time
from pageObjects.Customers import Castomers
from pageObjects.Login import Login
class Test_Costemors:
    URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = 'admin@yourstore.com'
    password = 'admin'
    email = 'test@12.com'
    name = 'test123'

    def test_addcustomer(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.Login = Login(self.driver)
        self.Login.set_user(self.username)
        self.Login.set_mp(self.password)
        self.Login.cnx_click()
        self.costemors = Castomers(self.driver)
        self.costemors.customer()
        self.costemors.add_click()
        self.costemors.set_email(self.email)
        self.costemors.set_name(self.name)
        self.costemors.Save_customer()
        message_ajouter = self.costemors.verif_ajouter()
        if message_ajouter.is_displayed():
            print('message ajouter est displayed')
            self.driver.close()
            assert True
        else:
            print('message ajouter est n pas displayed')
            self.driver.close()
            assert False

    def test_add_castom_table(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.costemors = Castomers(self.driver)
        self.Login = Login(self.driver)
        self.Login.set_user(self.username)
        self.Login.set_mp(self.password)
        self.Login.cnx_click()
        self.costemors.customer()
        self.costemors.add_click()
        self.costemors.set_email(self.email)
        self.costemors.set_name(self.name)
        self.costemors.Save_customer()
        time.sleep(2)
        n=self.costemors.nombre_rows_table()
        count=self.costemors.verifi_email_add(n,self.email)
        if count != 0 :
            print('ajouter avec succ')
            self.driver.save_screenshot("..\\Screeshots\\test_add_castom_table.png")
            self.driver.close()
            assert True
        else:
            print('ajouter n pas succ')
            self.driver.close()
            assert False





