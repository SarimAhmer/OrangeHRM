from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar


class AddUser:
    def __init__(self, driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)
        self.OrangeHRMLogin.login("Admin", "admin123")
        self.sidebar = SideBar(driver)
        self.sidebar.SideBarOptions("adminside")

    # create webdriver object and login
    def useradd(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        add = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        add.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'))
        )
        user_Role = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div')
        ActionChains(self.driver).move_to_element(user_Role).click(user_Role).perform()
        ActionChains(self.driver).move_to_element(user_Role).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).move_to_element(user_Role).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).move_to_element(user_Role).send_keys(Keys.RETURN).perform()

        name = self.driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
        name.send_keys(random.choice(string.ascii_letters))
        time.sleep(2)
        name.send_keys(Keys.ARROW_DOWN)
        name.send_keys(Keys.RETURN)
        name.send_keys(Keys.LEFT_CONTROL, 'a')
        name.send_keys(Keys.LEFT_CONTROL, 'c')

        status = self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
        ActionChains(self.driver).move_to_element(status).click(status).perform()
        ActionChains(self.driver).move_to_element(status).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).move_to_element(status).send_keys(Keys.RETURN).perform()

        userName = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
        userName.send_keys(Keys.LEFT_CONTROL, 'v')
        self.Name = userName.get_attribute('value')

        userPwd = self.driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
        userPwd.send_keys("Password123")

        userPwdConfirm = self.driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        userPwdConfirm.send_keys("Password123")
        userPwdConfirm.send_keys(Keys.RETURN)

    def VerifyUser(self):
        waitForCheck = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'))
        )
        checkUser = self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
        checkUser.send_keys(self.Name)
        checkUser.send_keys(Keys.RETURN)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        waitForUserCheck = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'))
        )

        createdUser = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div')
        self.userCheck = createdUser.text
        print(self.userCheck)
        return self.userCheck




if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    newUser = AddUser(driver)

    newUser.useradd()
    newUser.VerifyUser()

    driver.quit()