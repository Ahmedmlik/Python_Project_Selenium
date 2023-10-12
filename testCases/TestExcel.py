from pageObjects.Login import Login
from utilites.readProperties import ReadConfig
from utilites import XLUtils
import time

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\testData\\LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_user(self.user)
            self.lp.set_mp(self.password)
            self.lp.cnx_click()
            time.sleep(2)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.lp.logout()
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path,'Sheet1',r , 4,"Pass" )
                elif self.exp=='Fail':
                    self.lp.logout()
                    XLUtils.writeData(self.path,'Sheet1',r , 4,"Pass" )
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                elif self.exp == 'Fail':
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")

            print(lst_status)
        if "Fail" not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False