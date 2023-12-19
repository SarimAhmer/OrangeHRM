import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar

class DeleteUser:
    def __init__(self,driver):
        self.driver = driver
        self.orangeHRM = OrangeHRMLogin(driver)
        self.orangeHRM.login("Admin", "admin123")
        self.sidebar = SideBar(driver)
        self.sidebar.SideBarOptions("adminside")


    def delete_user(self):
        for i in range(50):
            # Wait to find Delete Button
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[1]'))
            )

            userDelete = self.driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[1]')
            ActionChains(self.driver).move_to_element(userDelete).click(userDelete).perform()

            # Wait for Dialog Box
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'))
            )

            deleteBtn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
            ActionChains(self.driver).move_to_element(deleteBtn).click(deleteBtn).perform()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    userDelete = DeleteUser(driver)

    userDelete.delete_user()

    driver.close()