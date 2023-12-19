from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar


class AdminTest:
    def __init__(self, driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)


    def doLogin(self):
        self.OrangeHRMLogin.login("Admin", "admin123")
        self.SideBar = SideBar(self.driver)
        self.SideBar.SideBarOptions("adminside")


    def SearchUser(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'))
        )
        new_user = self.driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
        role = self.driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        role.click()
        role.send_keys(Keys.ARROW_DOWN)
        role.send_keys(Keys.RETURN)
        status = self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]')
        status.click()
        status.send_keys(Keys.ARROW_DOWN)
        status.send_keys(Keys.RETURN)
        submit = self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        submit.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    adminTest = AdminTest(driver)

    adminTest.doLogin()
    adminTest.SearchUser()

    driver.quit()