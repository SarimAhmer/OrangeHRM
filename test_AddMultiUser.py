from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import names
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar



class AddMultiUser:
    def __init__(self,driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)
        self.OrangeHRMLogin.login("Admin", "admin123")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
        )
        self.sidebar = SideBar(driver)
        self.sidebar.SideBarOptions("adminside")
        self.Names = []

    def GenerateNames(self):
        for i in range(20):
            self.Names.append(names.get_first_name() + "123")


    def GoToAdd(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        add = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        add.click()
        time.sleep(2)


    def createNewUsers(self):
        self.GenerateNames()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div'))
        )
        for i in range(len(self.Names)):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]'))
            )
            user_Role = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]')
            ActionChains(self.driver).move_to_element(user_Role).click(user_Role).perform()
            ActionChains(self.driver).move_to_element(user_Role).send_keys(Keys.ARROW_DOWN).perform()
            ActionChains(self.driver).move_to_element(user_Role).send_keys(Keys.RETURN).perform()

            name = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
            name.send_keys(random.choice(string.ascii_letters))
            time.sleep(2)
            name.send_keys(Keys.ARROW_DOWN)
            name.send_keys(Keys.RETURN)

            status = self.driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
            ActionChains(self.driver).move_to_element(status).click(status).perform()
            ActionChains(self.driver).move_to_element(status).send_keys(Keys.ARROW_DOWN).perform()
            ActionChains(self.driver).move_to_element(status).send_keys(Keys.RETURN).perform()

            userName = self.driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
            Name = self.Names[i]
            userName.send_keys(Name)

            userPwd = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
            userPwd.send_keys("Password123")

            userPwdConfirm = self.driver.find_element(By.XPATH,
                                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
            userPwdConfirm.send_keys("Password123")
            userPwdConfirm.send_keys(Keys.RETURN)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
            )
            addnew = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
            addnew.click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    addusers = AddMultiUser(driver)

    addusers.GoToAdd()
    addusers.createNewUsers()

    driver.quit()