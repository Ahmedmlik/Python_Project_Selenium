from selenium.webdriver.common.by import By


class Castomers:
    btnmenucs = "(//p[contains(.,'Customers')])[1]"
    btcost = "(//p[contains(.,'Customers')])[2]"
    add = "//a[@href='/Admin/Customer/Create']"
    save = "(//i[contains(@class,'far fa-save')])[1]"
    email = "//input[@id='Email']"
    name = "//input[@id='FirstName']"
    lastname = "//input[@id='LastName']"
    nombre_table_rows = '//*[@id="customers-grid"]/tbody/tr'
    messgae_ajouter = '/html/body/div[3]/div[1]/div[1]'
    customerInfo_Xpath = '//div[@class="card-title"]'




    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        emailinput = self.driver.find_element(By.XPATH, Castomers.email)
        emailinput.clear()
        emailinput.send_keys(email)

    def set_name(self, name):
        name_input = self.driver.find_element(By.XPATH, Castomers.name)
        name_input.clear()
        name_input.send_keys(name)

    def add_click(self):
        add_button = self.driver.find_element(By.XPATH, Castomers.add)
        add_button.click()

    def customerInfo (self):
        btn_CI = self.driver.find_element(By.XPATH, Castomers.customerInfo_Xpath)
        btn_CI.click()


    def Save_customer(self):
        save = self.driver.find_element(By.XPATH, Castomers.save)
        save.click()

    def customer(self):
        menu_button = self.driver.find_element(By.XPATH, Castomers.btnmenucs)
        menu_button.click()
        customer_button = self.driver.find_element(By.XPATH, Castomers.btcost)
        customer_button.click()

    def nombre_rows_table(self):
        rowstable = self.driver.find_elements(By.XPATH, Castomers.nombre_table_rows)
        nombre = 0
        for i in rowstable :
            nombre += 1
        return nombre

    def verif_ajouter(self):
        message_ajouter = self.driver.find_element(By.XPATH, Castomers.messgae_ajouter)
        return message_ajouter

    def verifi_email_add(self,nb,email):

        for i in range(1,nb+1):
            count=0
            verif_email = self.driver.find_element(By.XPATH, f'//*[@id="customers-grid"]/tbody/tr[{i}]/td[2]')
            if verif_email.text == email :
                count+=1
                break

        return count



