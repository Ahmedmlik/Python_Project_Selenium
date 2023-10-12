from selenium.webdriver.common.by import By


class Login:
    user = "//input[contains(@id,'Email')]"
    mp = "//input[contains(@id,'Password')]"
    cnx = "//button[@class='button-1 login-button']"
    Logout = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_user(self, username):
        userinput = self.driver.find_element(By.XPATH, Login.user)
        userinput.clear()
        userinput.send_keys(username)

    def set_mp(self, mmp):
        mp_input = self.driver.find_element(By.XPATH, Login.mp)
        mp_input.clear()
        mp_input.send_keys(mmp)

    def cnx_click(self):
        cnx_button = self.driver.find_element(By.XPATH, Login.cnx)
        cnx_button.click()

    def logout (self) :
        logout = self.driver.find_element(By.XPATH, Login.Logout)
        logout.click()

